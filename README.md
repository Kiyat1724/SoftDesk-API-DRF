# SoftDesk API
> API REST sécurisée développée avec Django REST Framework pour la gestion collaborative de projets logiciels.
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-success)
![DRF](https://img.shields.io/badge/Django_REST_Framework-red)
![JWT](https://img.shields.io/badge/JWT-Secure-green)
![OpenClassrooms](https://img.shields.io/badge/OpenClassrooms-Projet_10-orange)

# Sommaire

- Présentation du projet
- Fonctionnalités
- Architecture
- Technologies et outils 
- Installation
- Authentification JWT
- Documentation des endpoints
- Exemples Postman
- Choix techniques
- Sécurité
- Green Code
- Améliorations futures


## Présentation du projet

SoftDesk API est une API REST développée avec **Django** et **Django REST Framework** dans le cadre du parcours **Développeur d'Application Python** d'OpenClassrooms.

Cette API permet de gérer des projets collaboratifs de développement logiciel. Les utilisateurs authentifiés peuvent créer des projets, ajouter des contributeurs, créer des issues (tickets) et échanger via des commentaires.

Le projet met en œuvre plusieurs bonnes pratiques de développement backend :

* authentification sécurisée avec JWT ;
* gestion des permissions selon les rôles des utilisateurs ;
* architecture modulaire Django ;
* utilisation de Nested Routers ;
* pagination des résultats ;
* optimisation des réponses grâce aux ListSerializer et DetailSerializer ;
* principes de Green Code et de Clean Code.

L'objectif est de proposer une API sécurisée, performante, facilement maintenable et conforme aux bonnes pratiques de développement d'une API REST professionnelle.
Ce projet a également été conçu comme un support d'apprentissage des bonnes pratiques de conception d'une API REST sécurisée, maintenable et évolutive.

## Fonctionnalités

L'API permet de réaliser les opérations suivantes :

### Gestion des utilisateurs

* Authentification par JWT
* Rafraîchissement des tokens
* Gestion des permissions selon l'utilisateur connecté

### Gestion des projets

* Créer un projet
* Consulter la liste des projets auxquels l'utilisateur participe
* Consulter le détail d'un projet
* Modifier un projet
* Supprimer un projet (uniquement par son auteur)

### Gestion des contributeurs

* Ajouter un contributeur à un projet
* Consulter les contributeurs d'un projet
* Modifier un contributeur
* Supprimer un contributeur

### Gestion des issues

* Créer une issue dans un projet
* Consulter les issues d'un projet
* Modifier une issue
* Supprimer une issue

### Gestion des commentaires

* Créer un commentaire sur une issue
* Consulter les commentaires d'une issue
* Modifier un commentaire
* Supprimer un commentaire

### Fonctionnalités techniques

* Authentification JWT
* Permissions personnalisées
* Nested Routers
* Pagination
* ListSerializer / DetailSerializer
* API REST sécurisée

## Architecture du projet

Le projet est organisé selon une architecture modulaire Django.

Chaque domaine fonctionnel possède sa propre application.

```
SoftDesk
│
├── softdesk/
│
├── projects/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│
├── issues/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│
├── comments/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt
```

Utilisateur
       │
       │ crée
       ▼
+------------------+
|     Project      |
+------------------+
        │
        │ possède
        ▼
+------------------+
|      Issue       |
+------------------+
        │
        │ contient
        ▼
+------------------+
|    Comment       |
+------------------+

Project
│
└── Contributors

### Pourquoi cette architecture ?

Chaque application possède une responsabilité unique :

* **projects** gère les projets et les contributeurs ;
* **issues** gère les tickets liés aux projets ;
* **comments** gère les commentaires associés aux issues.

Cette séparation respecte le principe de responsabilité unique (Single Responsibility Principle) et facilite la maintenance, les tests et l'évolution du projet.

## Technologies et outils 

### Langage

* Python 3.13

### Framework

* Django 6
* Django REST Framework

### Authentification

* JWT (JSON Web Token)
* djangorestframework-simplejwt

### Routage

* drf-nested-routers

### Documentation API

* drf-spectacular

### Base de données

* SQLite3

### Outils de développement 

* Git
* GitHub
* Postman
* VS Code

# Installation et configuration

## Prérequis

Avant d'installer le projet, assurez-vous de disposer des éléments suivants :

* Python 3.13 ou version supérieure
* Git
* pip
* Un environnement virtuel Python
* Postman (recommandé pour tester les endpoints de l'API)

---

## Cloner le dépôt

```bash
git clone https://github.com/Kiyat1724/SoftDesk-API-DRF.git

cd SoftDesk_API
```

---

## Créer un environnement virtuel

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Lorsque l'environnement est activé, le terminal affiche généralement :

```text
(venv)
```

---

## Installer les dépendances

Toutes les dépendances du projet sont référencées dans le fichier `requirements.txt`.

Installation :

```bash
pip install -r requirements.txt
```

Les principales bibliothèques utilisées sont :

* Django
* Django REST Framework
* Simple JWT
* DRF Nested Routers
* DRF Spectacular

---

## Variables d'environnement

Créer un fichier `.env` à la racine du projet.

Exemple :

```text
SECRET_KEY=your_secret_key
DEBUG=True
```

Le projet utilise `python-dotenv` afin de charger automatiquement ces variables.

> **Remarque :** en environnement de production, il est recommandé de désactiver `DEBUG` et de ne jamais versionner les informations sensibles.

---

## Initialiser la base de données

Créer les migrations :

```bash
python manage.py makemigrations
```

Appliquer les migrations :

```bash
python manage.py migrate
```

---

## Créer un superutilisateur

Créer un compte administrateur :

```bash
python manage.py createsuperuser
```

Ce compte permettra :

* d'accéder à l'administration Django ;
* d'obtenir un token JWT ;
* de réaliser les premiers tests fonctionnels.

---

## Lancer le serveur

```bash
python manage.py runserver
```

L'API sera disponible à l'adresse suivante :

```
http://127.0.0.1:8000/
```

L'administration Django est accessible via :

```
http://127.0.0.1:8000/admin/
```

---

## Vérification de l'installation

Après le lancement du serveur :

1. Vérifier que l'interface d'administration est accessible.
2. Vérifier que les migrations ont été correctement appliquées.
3. Vérifier qu'un utilisateur administrateur est présent.
4. Tester l'obtention d'un token JWT.
5. Tester les principaux endpoints avec Postman.

Si ces cinq étapes sont validées, l'installation est terminée.

# Authentification JWT

## Présentation

L'API utilise le mécanisme **JWT (JSON Web Token)** pour authentifier les utilisateurs.

Contrairement à une authentification basée sur les sessions, JWT permet de créer une API **stateless** : aucune session utilisateur n'est conservée côté serveur. Chaque requête contient un jeton d'accès qui permet d'identifier l'utilisateur.

Cette approche facilite l'intégration avec des applications web, mobiles ou des services tiers.

---

## Obtenir un token

Endpoint :

```http
POST /api/token/
```

Exemple de requête :

```json
{
    "username": "admin",
    "password": "mot_de_passe"
}
```

Réponse :

```json
{
    "refresh": "...",
    "access": "..."
}
```

---

## Rafraîchir un token

Endpoint :

```http
POST /api/token/refresh/
```

Exemple :

```json
{
    "refresh": "<refresh_token>"
}
```

---

## Utilisation du token

Toutes les routes protégées nécessitent un token JWT.

Dans Postman :

```
Authorization

Bearer Token

<access_token>
```

Le serveur authentifie automatiquement l'utilisateur avant d'exécuter la requête.

---

## Pourquoi avoir choisi JWT ?

Le choix de JWT présente plusieurs avantages :

* API sans gestion de session côté serveur ;
* authentification sécurisée ;
* meilleure évolutivité ;
* intégration simple avec des applications Front-End et mobiles ;
* standard largement adopté dans le développement d'API REST.

# Documentation des endpoints

L'API est organisée autour de quatre ressources principales :

* Projects
* Contributors
* Issues
* Comments

Les relations entre ces ressources sont représentées par des **Nested Routers**, ce qui permet de refléter la structure métier du projet.

## Authentification

| Méthode | Endpoint              | Description         |
| ------- | --------------------- | ------------------- |
| POST    | `/api/token/`         | Obtenir un JWT      |
| POST    | `/api/token/refresh/` | Rafraîchir un token |

---

## Projects

| Méthode | Endpoint              | Description                   |
| ------- | --------------------- | ----------------------------- |
| GET     | `/api/projects/`      | Liste des projets accessibles |
| POST    | `/api/projects/`      | Créer un projet               |
| GET     | `/api/projects/{id}/` | Consulter un projet           |
| PUT     | `/api/projects/{id}/` | Modifier un projet            |
| DELETE  | `/api/projects/{id}/` | Supprimer un projet           |

---

## Contributors

| Méthode | Endpoint                  |
| ------- | ------------------------- |
| GET     | `/api/contributors/`      |
| POST    | `/api/contributors/`      |
| PUT     | `/api/contributors/{id}/` |
| DELETE  | `/api/contributors/{id}/` |

---

## Issues

| Méthode | Endpoint                                        |
| ------- | ----------------------------------------------- |
| GET     | `/api/projects/{project_id}/issues/`            |
| POST    | `/api/projects/{project_id}/issues/`            |
| GET     | `/api/projects/{project_id}/issues/{issue_id}/` |
| PUT     | `/api/projects/{project_id}/issues/{issue_id}/` |
| DELETE  | `/api/projects/{project_id}/issues/{issue_id}/` |

---

## Comments

| Méthode | Endpoint                                                              |
| ------- | --------------------------------------------------------------------- |
| GET     | `/api/projects/{project_id}/issues/{issue_id}/comments/`              |
| POST    | `/api/projects/{project_id}/issues/{issue_id}/comments/`              |
| GET     | `/api/projects/{project_id}/issues/{issue_id}/comments/{comment_id}/` |
| PUT     | `/api/projects/{project_id}/issues/{issue_id}/comments/{comment_id}/` |
| DELETE  | `/api/projects/{project_id}/issues/{issue_id}/comments/{comment_id}/` |

# Exemples de tests avec Postman

Les tests fonctionnels de l'API ont été réalisés avec Postman.

Ordre recommandé des tests :

1. Obtenir un token JWT.
2. Créer un projet.
3. Ajouter un contributeur.
4. Créer une issue.
5. Ajouter un commentaire.
6. Vérifier les permissions.
7. Tester la pagination.

## Exemple de scénario

### 1. Authentification

```
POST /api/token/
```

↓

### 2. Création d'un projet

```
POST /api/projects/
```

↓

### 3. Création d'une issue

```
POST /api/projects/{project_id}/issues/
```

↓

### 4. Création d'un commentaire

```
POST /api/projects/{project_id}/issues/{issue_id}/comments/
```

Cette séquence reproduit le cycle de vie complet d'un projet collaboratif.

# Choix techniques

Cette API a été conçue en suivant les bonnes pratiques recommandées par Django REST Framework afin de proposer une architecture modulaire, évolutive et facilement maintenable.

## Architecture modulaire

Le projet est divisé en trois applications métier :

* **projects** : gestion des projets et des contributeurs ;
* **issues** : gestion des tickets liés aux projets ;
* **comments** : gestion des commentaires associés aux tickets.

Cette séparation applique le principe de responsabilité unique (Single Responsibility Principle), ce qui facilite la maintenance, les tests et l'évolution du projet.

---

## Django REST Framework

Le framework Django REST Framework a été retenu pour les fonctionnalités suivantes :

* ViewSets permettant de centraliser les opérations CRUD ;
* ModelSerializer réduisant la quantité de code à maintenir ;
* système de permissions intégré ;
* routage automatique via les Routers ;
* intégration simple avec JWT.

---

## Nested Routers

Les Nested Routers permettent de représenter les relations métier entre les différentes ressources.

Exemple :

```text
Project
   └── Issue
          └── Comment
```

Les URLs reflètent cette hiérarchie :

```text
/api/projects/{project_id}/issues/

/api/projects/{project_id}/issues/{issue_id}/comments/
```

Cette approche améliore la lisibilité de l'API et garantit que les ressources sont toujours manipulées dans leur contexte métier.

---

## ListSerializer et DetailSerializer

Deux serializers distincts ont été utilisés.

### ListSerializer

Les endpoints de liste renvoient uniquement les informations nécessaires.

Exemple :

* identifiant ;
* titre ;
* type.

Cette approche réduit le volume des données transférées et améliore les performances.

### DetailSerializer

Le serializer de détail renvoie l'ensemble des informations nécessaires lors de la consultation, de la création ou de la modification d'une ressource.

---

## perform_create()

Les champs sensibles ne sont jamais envoyés par le client.

Par exemple :

* `author_user`
* `project`
* `issue`

sont automatiquement renseignés côté serveur grâce à la méthode `perform_create()`.

Cette approche garantit la cohérence des données et limite les risques de manipulation côté client.

---

## Permissions personnalisées

Des permissions spécifiques ont été développées afin d'assurer le contrôle des accès.

Exemples :

* seuls les contributeurs d'un projet peuvent accéder à ses ressources ;
* seul l'auteur d'une ressource peut la modifier ou la supprimer.

Cette logique est implémentée dans des classes dédiées afin de séparer clairement les règles métier du reste de l'application.

# Sécurité

La sécurité constitue un élément essentiel de cette API.

Sans prétendre couvrir l'ensemble des recommandations OWASP ou garantir une conformité complète au RGPD, plusieurs bonnes pratiques ont été appliquées lors du développement.

## Authentification

L'API utilise JWT (JSON Web Token).

Chaque requête vers une ressource protégée nécessite un token valide.

Cette approche permet :

* une authentification sécurisée ;
* une API stateless ;
* une meilleure intégration avec des applications web ou mobiles.

---

## Contrôle des accès

L'accès aux ressources est contrôlé grâce à des permissions personnalisées.

Les utilisateurs ne peuvent consulter ou modifier que les ressources auxquelles ils sont autorisés à accéder.

Cette approche applique le principe du moindre privilège (Least Privilege Principle).

---

## Protection des données

Les relations entre les modèles utilisent les comportements adaptés :

* `PROTECT` pour empêcher la suppression de données critiques ;
* `CASCADE` lorsque la suppression d'une ressource doit entraîner celle de ses dépendances.

Cela garantit la cohérence de la base de données.

---

## Bonnes pratiques inspirées de l'OWASP

Le projet applique plusieurs recommandations du référentiel OWASP :

* authentification sécurisée avec JWT ;
* contrôle d'accès par permissions ;
* limitation des accès aux seules ressources autorisées ;
* validation des permissions avant chaque opération sensible.

---

## Principes compatibles avec le RGPD

Le projet applique plusieurs principes compatibles avec le RGPD :

* accès limité aux données autorisées ;
* minimisation des données renvoyées grâce aux ListSerializer ;
* séparation des responsabilités ;
* contrôle des opérations de modification.

Le projet étant un exercice pédagogique, il ne met pas en œuvre l'ensemble des exigences réglementaires du RGPD (gestion du consentement, droit à l'effacement, journalisation des traitements, etc.).

# Green Code

Le développement de cette API a été réalisé en tenant compte de plusieurs bonnes pratiques visant à limiter les traitements inutiles et à améliorer les performances.

## Pagination

Les endpoints de liste utilisent la pagination.

Cette approche permet :

* de limiter le nombre d'objets renvoyés ;
* de réduire la quantité de données transférées ;
* d'améliorer les performances côté serveur et côté client.

---

## ListSerializer

Les ListSerializer renvoient uniquement les informations nécessaires.

Cette stratégie réduit :

* la taille des réponses JSON ;
* le trafic réseau ;
* le temps de traitement.

---

## Filtrage des QuerySets

Chaque ViewSet filtre les données selon l'utilisateur connecté.

Par exemple, un utilisateur ne récupère que les projets auxquels il participe.

Cela évite les lectures inutiles en base de données et améliore les performances.

---

## Nested Routers

Les Nested Routers limitent naturellement les recherches aux ressources liées au contexte courant.

Par exemple :

```text
Projet
    └── Issues
             └── Commentaires
```

Les requêtes sont ainsi plus ciblées.

---

## Architecture modulaire

La séparation en plusieurs applications Django facilite :

* la maintenance ;
* l'évolution du projet ;
* la réutilisation du code.

Une architecture claire contribue également à limiter la complexité et les traitements inutiles lors des évolutions futures.

---

## Synthèse

Les principales pratiques de Green Code appliquées dans ce projet sont :

| Bonne pratique                    | Mise en œuvre |
| --------------------------------- | ------------- |
| Pagination                        | ✅             |
| ListSerializer                    | ✅             |
| Filtrage des QuerySets            | ✅             |
| Nested Routers                    | ✅             |
| Architecture modulaire            | ✅             |
| Réduction des données transférées | ✅             |
| Séparation des responsabilités    | ✅             |

# Perspectives d'évolution

Cette API a été développée dans le cadre d'un projet pédagogique. Son architecture modulaire permet toutefois d'envisager plusieurs évolutions afin de répondre aux besoins d'un environnement de production.

## Déploiement

* Déploiement sur une plateforme cloud (Azure, AWS, Render ou Railway).
* Configuration d'un environnement de production avec `DEBUG=False`.
* Gestion sécurisée des variables d'environnement.
* Utilisation d'un serveur WSGI/ASGI (Gunicorn, Uvicorn) derrière un serveur web tel que Nginx.

---

## Base de données

* Remplacement de SQLite par PostgreSQL pour améliorer les performances, la robustesse et la gestion de la concurrence.
* Mise en place de stratégies de sauvegarde et de restauration des données.

---

## Sécurité

* Mise en place d'un mécanisme de limitation du nombre de requêtes (Rate Limiting) afin de limiter les risques d'abus.
* Renforcement de la politique de gestion des secrets et des clés d'accès.
* Ajout de journaux d'audit (Audit Logs) afin de tracer les opérations sensibles.
* Revue régulière des dépendances pour appliquer les correctifs de sécurité.

---

## Qualité logicielle

* Développement de tests unitaires et de tests d'intégration afin d'améliorer la fiabilité de l'application.
* Mise en place d'une intégration continue (CI) avec GitHub Actions pour automatiser les tests et les vérifications à chaque modification du code.
* Analyse statique du code avec des outils de qualité afin de détecter précocement les anomalies.

---

## Documentation

* Génération d'une documentation interactive de l'API avec Swagger UI / OpenAPI.
* Publication de guides d'utilisation destinés aux développeurs et aux consommateurs de l'API.
* Mise à disposition d'une collection Postman facilitant la prise en main de l'application.

---

## Évolutions fonctionnelles

* Gestion avancée des rôles et des permissions.
* Système de notifications lors de la création ou de la mise à jour d'une issue.
* Ajout de filtres, de recherches et de tris sur les différentes ressources.
* Gestion des pièces jointes associées aux issues et aux commentaires.
* Historisation des modifications pour assurer une meilleure traçabilité.

---

## Conclusion

Ce projet m'a permis de mettre en pratique les principaux concepts de développement d'une API REST avec Django REST Framework : architecture modulaire, authentification JWT, permissions personnalisées, Nested Routers, pagination et optimisation des serializers.

Au-delà de la réalisation technique, ce projet m'a également permis de renforcer mes compétences en conception d'API, en sécurité applicative et en documentation technique, des compétences essentielles pour intervenir sur des projets professionnels et poursuivre mon évolution vers les métiers de la cybersécurité.

## Auteur

Projet réalisé par **Roukiat Said Hassani** dans le cadre du parcours
**Développeur d'Application Python** d'OpenClassrooms.

- GitHub : https://github.com/Kiyat1724
- LinkedIn : https://www.linkedin.com/in/roukiat-s-32bb52112
