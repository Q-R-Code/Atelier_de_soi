[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<img alt="Django" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img alt="Bootstrap" src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
<img alt="MySQL" src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
[![Build Status](https://app.travis-ci.com/Q-R-Code/Atelier_de_soi.svg?branch=main)](https://app.travis-ci.com/Q-R-Code/Atelier_de_soi)
--------------------------------------------------------------

# Atelier de Soi

Pour le projet final de la formation Développeur web Python de OpenClassRooms, j'ai choisi de réaliser une application
type Blog/Actualité dans le thème de l'Hypnose, la musicothérapie etc.

Ce projet fait suite à une envie, de faire découvrir cet univers, peu connus, aux personnes de ma région par le biais
d'une plateforme favorisant le partage et l'échange.

Dans cette application développée grâce au framework Django vous avez :

- Une page "accueil" pour, les spécialités, les acteurs (professionnels) qui vont alimenter le site et les actualités
  avec des articles.
- Une section blog pour publier des articles
- Un système de commentaires disponible sous chaque article pour échanger et discuter
- Utilisation du système authentification de Django pour attribuer des groupes selon les acteurs.

--------------------------------------------

## Utilisation ## 

L'utilisation de cette application est libre de droit.

Elle fournit une base modulable pour un site avec les fonctionnalités décrites ci-dessous, elle peut donc être
réutilisée pour un autre thème.

Pour réaliser la mise en forme, j'ai utilisé le template suivant : Gaia Bootstrap Template disponible
ici : https://www.creative-tim.com/product/gaia-bootstrap-template


--------------------------------------------

## Installation & lancement ##

Télécharger et décompresser le repository puis créer un VENV. Installer ensuite le requirements.

    pip install -r requirements.txt

Pour paramétrer la base de données il faut modifier les réglages dans atelier_de_soi_app settings.py > DATABASE.

Pour creer la base de données:

    python manage.py makemigrations && python manage.py migrate

Pour démarrer l'application :

    python manage.py runserver 

--------------------------------------------

## Applications  ##

### Account : ###

Gère la partie : inscription, connexion et déconnexion du site grace au système d'authentification de Django.
(django.contrib.auth).

### Blog : ###

Cette application s'occupe de la partie Blog du site.

- La création des tables BlogPost et Comment
- La gestion des articles et commentaires directement dans la page Admin de Django
- L'affichage des articles, des commentaires.
- Les templates nécessaires au Blog

### Main ### 

L'application principale, elle s'occupe de :

- Les templates pour l'accueil, l'actualité, les mentions légales
- La partie CSS/JS
- La table NewsPost
- La gestion des actualités dans Django admin
- L'affichage des trois dernières actualités sur la page d'accueil

--------------------------------------------

## Tests ##

Coverage : coverage.py v5.5, created at 2021-08-26 15:14 +0200 - 95%

    coverage run --omit='venv/*' --source='.' manage.py test
    coverage html -d 'nom'

- Utilisation de django-selenium-login pour forcer les connections durant les tests. ( une page 404 est visible lors du
démarrage des tests, c'est son comportement logique.)
- Utilisation de TravisCI pour l'automatisation des tests.

### Account ###

Des tests unitaires pour les vues : register et login.

Un test fonctionnel pour le parcours d'un utilisateur de la création de compte à la connexion.

### Blog ###

Un test fonctionnel pour le parcours d'un utilisateur connecté qui souhaite:

- Cliquer sur le menu "Blog" pour afficher les articles
- Cliquer sur le premier article
- Ajouter un commentaire

Un test d'intégration permet de vérifier le nombre de commentaires avant et apres l'ajout.
Des tests d'intégration sont aussi présent pour vérifier les vues : BlogList et BlogDetail


### Main ###

Un test fonctionnel pour le parcours d'un utilisateur connecté qui souhaite:

- Voir les actualités grâce au menu "Actualité"
- Cliquer sur la première actualité

Des tests d'intégrations sur les vues : home et legal_notice

--------------------------------------------

## Version : ##

- 1.0 : Premiere version stable de l'application. En ligne sur : 