import string

import emoji
import pymongo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk import WhitespaceTokenizer, SnowballStemmer, re
from nltk.corpus import stopwords

snow_stemmer = SnowballStemmer(language='spanish')
tweets_text = []
main_and_similar_tweets = []
finalCorpusStr = []
finalCorpus = []
similar_tweets = []
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_URI = "mongodb+srv://user:pass@cluster0.rqa40.mongodb.net/test"

cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=1000)
baseDatos = cliente["TFG"]
coleccion = baseDatos["Relacion_similares"]
coleccion2 = baseDatos["Tweet_similar"]


def clean(tweet):
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)  # Quitar @usuario
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)  # Quitar links http
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))  # Quitar signos de puntuación
    tweet = " ".join(tweet.split())
    tweet = emoji.demojize(tweet, delimiters=("", ""))
    # tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)  # Eliminar emojis

    tweet = tweet.replace("#", "").replace("_", " ")  # Quitar hastag pero dejando el texto

    return tweet


def delete_stop_words(array_tokens):
    stop_words = set(stopwords.words('spanish'))
    result = [t for t in array_tokens if not t in stop_words]
    return result


def lowercase(array_tokens):
    result = [t.casefold() for t in array_tokens]
    return result


def tokenization(tweet):
    # Tokenizamos despues de limpiar
    tokenizado = WhitespaceTokenizer().tokenize(tweet)
    return tokenizado


def stemmer(tokens_no_stop_words):
    stem_words = []
    for w in tokens_no_stop_words:
        x = snow_stemmer.stem(w)
        stem_words.append(x)

    return stem_words


def preprocess_tweets(tweets_array):
    for tweet in tweets_array:
        tweet['texto'] = clean(tweet["texto"])

        tokenized = tokenization(tweet['texto'])

        lowercase(tokenized)

        no_stop_words = delete_stop_words(tokenized)

        stemized = stemmer(no_stop_words)

        finalCorpus.append(stemized)


def group_tweets(tweets_array):
    i = 0

    aux = tweets_array.copy()

    if len(aux) > 1:
        del aux[0]
        preprocess_tweets(tweets_array)
        for f in finalCorpus:
            stri = " ".join(f)
            finalCorpusStr.append(stri)
        finalQuerieStr = finalCorpusStr[0]
        del finalCorpusStr[0]
        mytfidf_vectorizer = TfidfVectorizer()
        matriz_tfidf = mytfidf_vectorizer.fit_transform(finalCorpusStr)
        matriz_tfidfarr = matriz_tfidf.toarray()

        query_tfidf = mytfidf_vectorizer.transform([finalQuerieStr])
        query_tfidfarr = query_tfidf.toarray()

        cosenoTFIDF = cosine_similarity(query_tfidf, matriz_tfidf)
        # print(cosenoTFIDF.shape)
        # print(len(aux))
        for val in cosenoTFIDF[0]:
            if val > 0.2:
                similar_tweets.append(
                    {'_id': aux[i]['_id'], 'texto': aux[i]['texto'],
                     'total_interacciones': aux[i]['total_interacciones'],
                     'distancia_coseno': val})
                del aux[i]
                i = i - 1
            i = i + 1
            # print(i)
        if len(similar_tweets) > 0:
            coleccion2.insert_many(similar_tweets)
        coleccion.insert_one({'_id': tweets_array[0]['_id'],
                              'usuario': tweets_array[0]['usuario'],
                              'tweet_principal_texto': tweets_array[0]['texto'],
                              'tweet_principal_interacciones': tweets_array[0]['total_interacciones'],
                              'tweets_similares': similar_tweets})
        # print(len(aux))
        finalCorpus.clear()
        finalCorpusStr.clear()
        similar_tweets.clear()
        group_tweets(aux)

    else:
        return main_and_similar_tweets
