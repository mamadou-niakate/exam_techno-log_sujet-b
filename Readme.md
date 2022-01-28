
# Comment utiliser l'API

| Méthode | URL                     | Description                                           |
|---------|-------------------------|-------------------------------------------------------|
| GET     | /jeux                   | Récupérer la liste des jeux                           |
| POST    | /jeux                   | Ajouter un jeu                                        |
| GET     | /jeux/:id               | Récupérer un jeu                                      |
| GET     | /jeux/?cond=inf&prix=10 | Récupérer les jeux dont le prix est inferieur à un 10 |
| GET     | /jeux/?cond=sup&prix=10 | Récupérer les jeux dont le prix est supérieur à un 10 |


## Il faut utiliser une application comme postman afin d'executer des requête

### Ajouter un jeu
![alt ajout_jeu](./screen_shots/Capture%20d’écran%20de%202022-01-28%2014-42-08.png)

### Récupérer la liste des jeux : Postman ou navigateur 
![alt get_jeux](./screen_shots/all_games.png)

### Récupérer la liste des jeux par rapport à un prix
#### Supérieur à un prix
![alt jeux_prix_sup_a](./screen_shots/prix_sup_a.png)
#### Inférieur à un prix
![alt jeux_prix_in_a](./screen_shots/prix_inf_a.png)