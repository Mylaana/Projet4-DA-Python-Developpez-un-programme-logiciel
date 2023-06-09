# Projet4-DA-Python-Développez-un-programme-logiciel

## Scénario
En tant que développeur, je suis missionné pour créer un programme de gestion de tournois d'échecs avec les contraintes suivantes :

- le programme doit pouvoir être éxecuté hors ligne
- être développé selon les principes du pattern "MVC"
- utiliser un systèeme de sauvegarde/chargement à chaque action de l'utilisateur
- respecter la PEP8 et utiliser flake8 comme linter



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
python main.py
```

markdown
Copy code

5. Suivez les instructions qui s'affichent dans la console pour naviguer dans le programme.

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
