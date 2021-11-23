# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import locale

import pymongo
import tweepy
import agruparTweets
import time
from datetime import timedelta, datetime
from operator import itemgetter
import nltk
from nltk.corpus import stopwords
import extractTweetsTwarc

locale.setlocale(locale.LC_ALL, 'esp_esp')
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_URI = "mongodb+srv://user:pass@cluster0.rqa40.mongodb.net/test"

cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=1000)
baseDatos = cliente["TFG"]
coleccion = baseDatos["Entidades"]

with open('entidades.json', encoding='utf8') as json_file:
    entidades_data = json.load(json_file)

entidades_a_mostrar = []
nombre_entidades_recuperadas = []
tweets = []
while True:
    tipo_entidad_introducido = input(
        "Introduce un tipo de Entidad de los siguientes: PERSON, LOCATION, ORGANIZATION, EVENT, "
        "WORK_OF_ART, "
        "CONSUMER_GOOD, PHONE_NUMBER, ADDRESS, DATE, NUMBER, PRICE \n")
    if tipo_entidad_introducido.upper() not in (
            'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'PHONE_NUMBER', 'ADDRESS',
            'DATE',
            'NUMBER', 'PRICE'):
        print("Tipo de Entidad INCORRECTO. Por favor asegurate de que estan escritos igual que te los menciono")
        continue
    else:
        print("A continuación se mostrarán las Entidades extraidas con el tipo que has seleccionado")
        for entidad in entidades_data:
            nombre_entidades_recuperadas.append(entidad['nombre'])
            if entidad['tipo'].upper() == tipo_entidad_introducido.upper() and entidad[
                'nombre'] not in entidades_a_mostrar:
                entidades_a_mostrar.append(entidad['nombre'])
                print(entidad['nombre'])
    otra_entidad = input("¿Quieres ver resultados de otro tipo de entidades?, Escribe yes/no\n")
    if otra_entidad.lower() == 'yes':
        entidades_a_mostrar = []
        continue
    elif otra_entidad.lower() == 'no':
        break

while True:
    entidad_seleccionada = input("Introduce la entidad sobre la que quieres ver tweets:\n")
    if entidad_seleccionada in entidades_a_mostrar:
        # Recuperar tuits de la entidad
        e = []
        print("Estos son los titulares y las fechas donde aparece la entidad seleccionada\n")
        for entidad in entidades_data:
            if entidad['nombre'].upper() == entidad_seleccionada.upper():
                e.append({entidad['titular'], entidad['fecha']})
                print("TITULAR: " + entidad['titular'] + " FECHA:" + entidad['fecha'])
                coleccion.insert_one({'nombre_entidad': entidad['nombre'],
                                      'titular_origen': entidad['titular'],
                                      'fecha': datetime.strptime(entidad['fecha'], '%Y-%m-%d %H:%M:%S').strftime("%d/%m/%Y"),
                                      'origen': entidad['origen']
                                      })

        fecha_introducida = input("Introduce la fecha escogida de los titulares anteriores(YYYY-MM-DD), "
                                  "para poder extraer los tweets\n")
        print("Buscando Tweets...")
        tweets = extractTweetsTwarc.extraer_y_almacenar_tweets(fecha_introducida, entidad_seleccionada)
        break
    else:
        print("Entidad incorrecta, asegurate de escribir la entidad igual que se muestra\n")
        continue
print("Agrupando tweets")

if tweets is not None:
    agruparTweets.group_tweets(tweets)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
