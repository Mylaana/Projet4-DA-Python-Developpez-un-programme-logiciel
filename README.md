# Projet4-DA-Python-Développez-un-programme-logiciel

Description concise du projet.

## Exécution du Programme

1. Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez le télécharger à partir de [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. Clonez ce dépôt GitHub sur votre machine locale :

git clone https://github.com/votre-utilisateur/nom-du-depot.git

bash
Copy code

3. Accédez au répertoire du projet :

cd nom-du-depot

markdown
Copy code

4. Exécutez le programme Python en utilisant la commande suivante :

python nom_du_programme.py

markdown
Copy code

5. Suivez les instructions qui s'affichent dans la console pour naviguer dans le programme.

## Génération du rapport Flake8

1. Assurez-vous d'avoir Flake8 installé. Vous pouvez l'installer en utilisant la commande suivante :

pip install flake8

bash
Copy code

2. Accédez au répertoire du projet :

cd nom-du-depot

markdown
Copy code

3. Pour générer le rapport Flake8 avec une limite de 119 caractères, exécutez la commande suivante :

flake8 --format=html --htmldir=flake-report --max-line-length 119

Le rapport sera affiché dans la console avec les détails sur les erreurs et les avertissements liés au style de code.



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