# Projet Mercadona

Ce dépôt contient le projet d'application correspondant au bloc 3 - Développement d'une solution digitale avec Python

## Structure de l'application

L'application a été créée avec Django.

Le Back-end est effectué en python.

La base de donnée fonctionne avec PostgreSql.

Côté front, on retrouve du HTML/CSS/Bootstrap.

## Fonctionnement de l'application

### Côté ADMIN
Depuis l'URL : http://127.0.0.1:8000/admin on arrive sur la page admin qui permet d'ajouter des produits, des catégories mais aussi des promotions.

### Côté USER
Depuis l'URL : http://127.0.0.1:8000/ on arrive sur la page où l'on retrouve tous les produits ajoutés par l'admin et leur prix. On y voit également les promotions avec leur prix en rouge, mais aussi une liste de catégories qui permet de filtrer les produits en fonction de la catégorie à laquelle ils appartiennent.


## Exécution de l'application

Voici les prérequis :

1. Python3
2. Installez Django : 
```
pip install django
```
3. Installez PostgreSql
4. Créer une nouvelle base de données dans PostgreSql
5. Créer un fichier .env
6. Ajouter les données suivantes à l'intérieur 

SECRET_KEY = La clé secrète django à ne pas divulguer en tant normal --> django-insecure-g53fmjgz#f2q4mcfl-o*jimlqc@l#sxdw7&@(xlim0mo*54z^p

DB_NAME = Le nom de votre base de donnée créée dans PostgreSql

DB_USER = Votre nom d'utilisateur PostgreSql

DB_PASSWORD = Votre mot de passe PostgreSql

DB_HOST=127.0.0.1

DB_PORT=5432

DATABASE_URL=postgres://mercadona:9xYfFA2cDGs1FP4@mercadona-db.flycast:5432/mercadona
7. Migrer les données :
```
python manage.py migrate
```
```
python manage.py makemigrations
```
8. Lancer l'application : 
```
python manage.py runserver
```