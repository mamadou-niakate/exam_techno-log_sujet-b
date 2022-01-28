from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
# from uuid import uuid4
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
        jeux_to_send.append(
            {"console": jeu["console"], "genre": jeu["genre"], "prix": jeu["prix"], "description": jeu["description"],
             "code_rayon": jeu["code_rayon"]})
    return jeux_to_send


@app.get("/jeux/filter")
def get_jeux(cond: str, prix: int):
    jeux = col.find()
    jeux_to_send = []

    if cond == "sup":
        for jeu in jeux:
            if prix < jeu['prix']:
                jeux_to_send.append({"console": jeu["console"], "genre": jeu["genre"], "prix": jeu["prix"],
                                     "description": jeu["description"], "code_rayon": jeu["code_rayon"]})
    if cond == "inf":
        for jeu in jeux:
            if jeu['prix'] < prix:
                jeux_to_send.append({"console": jeu["console"], "genre": jeu["genre"], "prix": jeu["prix"],
                                 "description": jeu["description"], "code_rayon": jeu["code_rayon"]})
    return jeux_to_send


@app.post("/jeux")
def add_jeu(jeu: ModelJeu):
    jeu_ss_exists = col.find_one({"prix": jeu.prix})
    if jeu_ss_exists:
        raise HTTPException(500)
    else:
        # unique_id = str(uuid4())
        # print(unique_id)
        jeu = {"console": jeu.console, "genre": jeu.genre, "prix": jeu.prix, "description": jeu.description,
               "code_rayon": jeu.code_rayon}
        print(jeu)
        col.insert_one(jeu)


@app.get("/jeux/{prix}")
def get_jeu(prix: float):
    jeu = col.find_one({"prix": prix})
    return {"console": jeu['console'], "genre": jeu['genre'], 'prix': jeu['prix'], "description": jeu["description"],
            "code_rayon": jeu["code_rayon"]}


@app.delete("/jeux/{prix}")
def delete_jeu(prix: float):
    col.find_one_and_delete({"prix": prix})


@app.put("/jeux/{prix}")
def update_jeu(prix: str, jeu: ModelJeu):
    col.find_one_and_update({'prix': prix}, {
        "$set": {'console': jeu.console, 'genre': jeu.genre, 'prix': jeu.prix, "description": jeu.description,
                 "code_rayon": jeu.code_rayon}})
