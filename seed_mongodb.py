import pymongo
# Import de la classe MongoClient qui nous permettra de nous connecter a la base de donnees MongoDB
from pymongo import MongoClient

client = MongoClient(host="c_mongo_exam")

# Acces a la base de donnees 'some_db'
db = client["jeux_db"]

# Acces a la collection 'some_col'
col = db["jeux"]

# Ajout d'un 'fruit' dans la collection
jeux = [
    {
        "console":"console 1",
        "genre":"sport",
        "prix":13.28,
        "description": "another cool description",
        "code_rayon": "AFR.21.42.2013"
    },
    {
        "console":"another real console",
        "genre":"simulation",
        "prix":20,
        "description": "this is a description",
        "code_rayon": "EUR.13.07.2021"
    },
    {
        "console":" RPG console",
        "genre":"RPG",
        "prix":5,
        "description": "this is a description",
        "code_rayon": "USA.13.07.2021"
    }
]
res = col.insert_many(jeux)

# Verification de l'ajout
print('les jeux {} ont bien ete crees'.format(res.inserted_ids))