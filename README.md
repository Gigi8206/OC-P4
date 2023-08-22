![Python Version](https://img.shields.io/badge/Python-3.7-blue.svg)![Flake8](https://img.shields.io/badge/Flake8-Passing-brightgreen.svg)
# Gestionnaire de Tournoi d'Échecs

## Table des matières

- [Introduction](#introduction)
- [Configuration requise](#configuration-requise)
- [Installation](#installation)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#structure-du-projet)
- [Utilisation](#utilisation)
- [Rapport Flake8](#rapport-flake8)

## Introduction

Le Gestionnaire de Tournoi d'Échecs est un logiciel Python permettant de gérer des tournois d'échecs selon le système de tournoi "suisse". Il a été développé dans le cadre d'un projet visant à aider un club d'échecs local à organiser ses tournois de manière plus efficace et conviviale. Le programme offre des fonctionnalités pour créer, gérer et sauvegarder des tournois, ajouter des joueurs, lancer des matchs, saisir les résultats et afficher le classement des joueurs.

## Configuration requise

* Python 3 installé sur votre système : [Téléchargement Python 3](https://www.python.org/downloads/)
* Git installé sur votre système : [Téléchargement Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Installation

1. Téléchargez et installez Python 3 depuis le site officiel : https://www.python.org/downloads/
2. Ouvrez l'invite de commande (ou terminal).
3. Créez un dossier pour l'application avec la commande : `mkdir GestionnaireTournoiEchecs`.
4. Accédez au dossier nouvellement créé : `cd GestionnaireTournoiEchecs`.
5. Créez un environnement virtuel avec la commande (Windows) : `python -m env .env` ou (Mac/Linux) : `python3 -m env .env`.
6. Activez l'environnement virtuel (Windows) : `.env\Scripts\activate` ou (Mac/Linux) : `source .env/bin/activate`.
7. Installez les dépendances requises avec la commande : `pip install -r requirements.txt`.
8. Ajoutez les fichiers du Gestionnaire de Tournoi d'Échecs dans le dossier.

ou :

1. Téléchargez le projet sur votre répertoire local : 
```
git clone https://github.com/MarcOutt/OC_p4.git
```

2. Mettez en place un environnement virtuel :
   * Créez l'environnement virtuel: `python -m venv env`
   * Activez l'environnement virtuel :
       * Windows : `env\Scripts\activate.bat`
       * Unix/MacOS : `source env/bin/activate`

3. Installez les dépendances du projet :

```
pip install -r requirements.txt
```
