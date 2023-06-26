# Projet4-DA-Python-Développez-un-programme-logiciel

Description concise du projet.

## Exécution du Programme

1. Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez le télécharger à partir de :
[https://www.python.org/downloads/](https://www.python.org/downloads/).

2. Clonez ce dépôt GitHub ou télécharger ses fichiers sur votre machine locale

3. Accédez au répertoire du projet :

```
cd nom-du-repertoire-du-depot
```
  
4. Exécutez le programme Python en utilisant la commande suivante :

```
python nom_du_programme.py
```

5. Le programme utilise des menus/listes d'options pour naviguer.
   Chaque liste d'options est structuré avec un chiffre/lettre suivi de la description de l'option.
   Entrez le caractere qui correspond à votre choix et appuyez sur entrée.
   Vous serez également amené à entrer des informations comme le nom du tournoi, les informations des joueurs.

## Génération du rapport Flake8

1. Assurez-vous d'avoir Flake8 et flake8-html installés. Vous pouvez les installer en utilisant les commandes suivantes :

```
pip install flake8
pip install flake8-html
```

2. Accédez au répertoire du projet :

```
cd nom-du-repertoire-du-depot
```

3. Pour générer le rapport Flake8 avec une limite de 119 caractères dans des fichiers html, exécutez la commande suivante :
```
flake8 --format=html --htmldir=flake-report --max-line-length 119
```
   Le rapport sera édité dans un dossier "flake-report" dans le repertoire du programme.



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
