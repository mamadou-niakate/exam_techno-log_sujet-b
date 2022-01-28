from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from ModelJeu import ModelJeu

client = MongoClient(host="c_mongo_exam")

db = client["jeux_db"]

col = db["jeux"]

app = FastAPI()


@app.get("/jeux")
def get_jeux():
    jeux = col.find()
    jeux_to_send = []

    for jeu in jeux:
        jeux_to_send.append({"console":jeu["console"],"genre":jeu["genre"],"prix":jeu["prix"],"description":jeu["description"],"code_rayon":jeu["code_rayon"]})
    return jeux_to_send


@app.post("/jeux")
def add_jeu(jeu: ModelJeu):
    jeu_ss_exists = col.find_one({"prix": jeu.prix})
    if jeu_ss_exists:
        raise HTTPException(500)
    else:
        col.insert_one({"console": jeu.console, "genre": jeu.genre, "prix": jeu.prix, "description":jeu.description,"code_rayon":jeu.code_rayon})


@app.get("/jeux/{prix}")
def get_jeu(prix: float):
    jeu = col.find_one({"prix": prix})
    return {"console":jeu['console'],"genre":jeu['genre'],'prix':jeu['prix'],"description":jeu["description"],"code_rayon":jeu["code_rayon"]}


@app.delete("/jeux/{prix}")
def delete_jeu(prix: float):
    col.find_one_and_delete({"prix": prix})


@app.put("/jeux/{prix}")
def update_jeu(prix: str, jeu: ModelJeu):
    col.find_one_and_update({'prix':prix}, {"$set":{'console': jeu.console, 'genre': jeu.genre, 'prix': jeu.prix, "description":jeu.description,"code_rayon":jeu.code_rayon}})