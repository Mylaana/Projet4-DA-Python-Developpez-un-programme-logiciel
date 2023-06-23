# Projet4-DA-Python-Développez-un-programme-logiciel

# Description de la structure du code :  
## Pattern MVC :  
## Module main de haut niveau  
- initialise les controllers et leurs passe leurs models et views.

## Controller tournament :  
- 1 model
- 1 view
- 1 objet save_load

## Controller player :  
- 1 model player_list + 1 player class manipulée par player_list
- 1 view
- 1 objet save_load

## Controller round :  
- 1 model round + 1 match class manipulée par player_list
- 1 view
- 1 objet save_load

## classe save_load
- gere les ecritures / lectures du fichier .json du tournois
- les fonctions update_all/load_all permettent de lancer les fonctions correspondantes de chaque model.


# pour finaliser :
to do :
-blinder les menu selection
-checker tous les choix



flake8 --format=html --htmldir=flake-report --max-line-length 119