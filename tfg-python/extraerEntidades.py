import glob
import json

import nltk
from google.cloud import language_v1
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

read_files = glob.glob("./Titulares/*.json")
entidades = []

client = language_v1.LanguageServiceClient()
type_ = language_v1.Document.Type.PLAIN_TEXT
for file in read_files:
    myjson = open(file, encoding="utf8")
    data = myjson.read()
    obj = json.loads(data)
    for elem in obj:
        titular = elem['titular']
        fecha = elem['fecha']
        origen = ""
        if type(elem['origen']) is list and len(elem['origen']) > 0:
            origen = elem['origen'][0]
        elif type(elem['origen']) is str:
            origen = elem['origen']

        document = {"content": titular, "type_": type_}

        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_entities(request={'document': document, 'encoding_type': encoding_type})

        # Recorremos las entidades devueltas por la API
        for entity in response.entities:
            if entity.name not in stop_words:
                e = {'titular': titular, 'nombre': entity.name, 'tipo': language_v1.Entity.Type(entity.type_).name,
                     'fecha': fecha, 'origen': origen}
                entidades.append(e)
                print("Entidad: ", e)
            # print(e.nombre)
            # print(e.tipo)
            # print(listaEntidades[0].nombre)
            # print(u"Entidad: {}".format(entity.name))

            # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
            # print(u"Tipo de entidad: {}".format(language_v1.Entity.Type(entity.type_).name))

with open('entidades.json', 'w', encoding='utf8') as outfile:
    json.dump(entidades, outfile)
