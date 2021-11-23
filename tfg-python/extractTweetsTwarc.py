import json

import twarc
from datetime import datetime, timedelta
import datetime as dt
from twarc import ensure_flattened
import pymongo
from google.cloud import language_v1
import agruparTweets
import csv
from operator import itemgetter
import dateutil.parser
import pprint
from langdetect import detect

tweets_for_wordcloud = []
tweets_corpus = []
fechas_tweets = []
sentimiento_tweets = []
localizacion_tweets = []
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_URI = "mongodb+srv://user:pass@cluster0.rqa40.mongodb.net/test"

cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=1000)
baseDatos = cliente["TFG"]
coleccion = baseDatos["Tweets"]
coleccion2 = baseDatos["Entidades"]


def generar_wordcloud(tweets):
    string_tweets_words = ""
    aux = []
    for f in tweets:
        stri = " ".join(f)
        string_tweets_words = string_tweets_words + stri + " "
    # Transformamos el string de todos los tweets a array de palabras
    lista_palabras = string_tweets_words.split()

    # Sacamos una lista de palabras únicas
    unique_words = set(lista_palabras)

    for words in unique_words:
        aux.append({'text': words, 'value': lista_palabras.count(words)})
    with open("wordcloud.json", 'w', encoding='utf-8') as outfile:
        json.dump(aux, outfile)


def contar_tweets(lista_fechas):
    aux = []
    unique_dates = set(lista_fechas)
    for fecha in unique_dates:
        aux.append({'fecha': fecha, 'numero_tweets': lista_fechas.count(fecha)})
    aux = sorted(aux, key=lambda date: datetime.strptime(date['fecha'], "%d/%m/%Y"))
    with open('numero_tweets_dia.json', 'w', encoding='utf-8') as outfile:
        json.dump(aux, outfile)


def contar_sentimiento(lista_sentimiento):
    aux = []
    unique_sentiment = ["muy negativo", "negativo", "neutral", "positivo", "muy positivo"]
    for sentimiento in unique_sentiment:
        aux.append({'sentimiento': sentimiento, 'numero': lista_sentimiento.count(sentimiento)})
    with open('sentimiento_tweets.json', 'w', encoding='utf-8') as outfile:
        json.dump(aux, outfile)


def contar_localizacion(lista_localizacion):
    aux = []
    unique_localizacion = set(lista_localizacion)
    for localizacion in unique_localizacion:
        aux.append({'localizacion': localizacion, 'numero': lista_localizacion.count(localizacion)})
    with open('localizacion_tweets.json', 'w', encoding='utf-8') as outfile:
        json.dump(aux, outfile)


def analizar_sentimiento(tweet_text):
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(content=tweet_text, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    # Print the results
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return [score, magnitude]


def extraer_y_almacenar_tweets(fecha_inicio, entidad):
    extracted_tweets = []
    contador_pagina = 0
    bearer_token = "AAAAAAAAAAAAAAAAAAAAALHhNAEAAAAA3qYOmH2lMrSAs%2FBqhTI%2FEOGfbEg%3DcfWmaR4P6R0C4OLJqMjQo049v3V5J1z8AhYn9C5YKdAhj0f1DM"
    t = twarc.Twarc2(
        bearer_token=bearer_token,
    )
    # Busqueda centrada en encontrar tweets relacionados con el bulo
    start = datetime.strptime(fecha_inicio, "%Y-%m-%d") + timedelta(days=-3)
    end = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    search_results = t.search_all(query=entidad + ' -is:retweet lang:es', start_time=start,
                                  end_time=end, max_results=100)

    # Busqueda centrada en encontrar todos los tweets durante 7-8 dias
    # para ver el numero de tweets que se han escritos relacionados con la entidad consultada
    extend_start = datetime.strptime(fecha_inicio, "%Y-%m-%d") + timedelta(days=-4)
    extend_end = datetime.strptime(fecha_inicio, "%Y-%m-%d") + timedelta(days=3)
    extend_search_results = t.search_all(query=entidad + ' -is:retweet lang:es',
                                         start_time=extend_start, end_time=extend_end, max_results=100)
    print("Contando el numero de tweets desde 4 dias antes de la noticia del bulo hasta 3 dias despues")
    for page in extend_search_results:
        for tweet in ensure_flattened(page):
            d = dateutil.parser.parse(tweet['created_at'])
            fecha = datetime.strftime(d, '%m/%d/%Y')
            fecha = datetime.strptime(fecha, '%m/%d/%Y').strftime("%d/%m/%Y")
            fechas_tweets.append(fecha)

    # Por cada pagina el maximo de resultados obtenidos es max_results->valor entre 10 y 500.
    print(
        "Extrayendo y calculando la informacion de los tweets desde 3 dias antes a la publicacion de la noticia sobre el bulo")
    for page in search_results:
        # if contador_pagina <= 10:
        for tweet in ensure_flattened(page):
            tweet['text'] = agruparTweets.clean(tweet["text"])
            tokenized = agruparTweets.tokenization(tweet['text'])
            lowercase = agruparTweets.lowercase(tokenized)
            no_stop_words = agruparTweets.delete_stop_words(lowercase)
            tweets_corpus.append(no_stop_words)

            total_interacciones = tweet['public_metrics']['retweet_count'] + tweet['public_metrics']['like_count'] + \
                                  tweet['public_metrics']['reply_count'] + tweet['public_metrics']['quote_count']

            my_tweet = {'_id': tweet['id'],
                        'usuario': tweet['author']['username'],
                        'n_retweets': tweet['public_metrics']['retweet_count'],
                        'n_likes': tweet['public_metrics']['like_count'],
                        'n_respuestas': tweet['public_metrics']['reply_count'],
                        'n_menciones': tweet['public_metrics']['quote_count'],
                        'texto': tweet['text'],
                        'fecha': tweet['created_at'],
                        'total_interacciones': total_interacciones,
                        'link_tweet': "https://twitter.com/iniciarsesion/status/" + tweet['id']}

            if 'geo' in tweet:
                my_tweet['localizacion'] = tweet['geo']['country']
                localizacion_tweets.append(tweet['geo']['country'])

            if detect(my_tweet['texto']) == "es":
                resultados = analizar_sentimiento(my_tweet['texto'])
                if 0 <= resultados[0] < 0.1 or -0.1 < resultados[0] <= 0:
                    my_tweet['sentimiento'] = 'neutral'
                    sentimiento_tweets.append('neutral')
                if 0.1 <= resultados[0] <= 0.5:
                    my_tweet['sentimiento'] = 'positivo'
                    sentimiento_tweets.append('positivo')
                if 0.5 < resultados[0] <= 1:
                    my_tweet['sentimiento'] = 'muy positivo'
                    sentimiento_tweets.append('muy positivo')
                if -0.5 <= resultados[0] <= -0.1:
                    my_tweet['sentimiento'] = 'negativo'
                    sentimiento_tweets.append('negativo')
                if -1 <= resultados[0] < -0.5:
                    my_tweet['sentimiento'] = 'muy negativo'
                    sentimiento_tweets.append('muy negativo')

            if total_interacciones > 1:
                coleccion.insert_one(my_tweet)
                extracted_tweets.append(my_tweet)
        contador_pagina = contador_pagina + 1
        print("Pasando a la siguiente página de tweets encontrados")
    # else:
    print("Generando archivo json para representar el wordcloud")
    generar_wordcloud(tweets_corpus)
    print("Generando archivo json para representar el numero de tweets por dia")
    contar_tweets(fechas_tweets)
    print("Generando archivo json para representar el sentimiento de los tweets")
    contar_sentimiento(sentimiento_tweets)
    print("Generando archivo json para representar el numero de tweets emitidos por localizacion")
    contar_localizacion(localizacion_tweets)
    extracted_tweets = sorted(extracted_tweets, key=itemgetter('total_interacciones'), reverse=True)
    ##print(extracted_tweets)
    return extracted_tweets
