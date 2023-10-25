# kubernetes-devops-project

If you come from the Kubernetes training, you're in the right place ! :) 

Run the application :

```python
docker-compose up -d
```

## Initialiser le projet

```python
# Run the application
docker-compose up -d

# Stop the application
docker-compose down

# Supprimer l'image construite
docker image rm dst-k8s-devops-project_fastapi

# Verify images and containers
clear && docker image ls && echo "" && docker container ls && echo ""

# Run the l'application en forcant le build
docker-compose up -d --build
```

## Optimiser l'image

`Dockerfile` avant :

```dockerfile
FROM python:3.8.10
 
WORKDIR /app
COPY . /app
 
RUN python -m pip install pip==20.0.2
RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
```

`Dockerfile` apres :

```dockerfile
# Étape 1 : Construction de l'environnement
FROM python:3.8.10 as builder

WORKDIR /app
COPY requirements.txt .

# Mettre à jour pip et installer les dépendances dans /build
RUN python -m pip install --upgrade pip==20.0.2
RUN pip install --prefix=/install -r requirements.txt

# Étape 2 : Image finale basée sur Alpine
# FROM python:3.8.10-alpine3.14
FROM python:3.8.10-slim-buster

# Copier les fichiers de l'étape de construction
COPY --from=builder /install /usr/local

WORKDIR /app
COPY . .

# Exposer le port
EXPOSE 5000

# Commande de démarrage
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
```

```python
# Avant optimisation
docker image ls

REPOSITORY                       TAG           IMAGE ID       CREATED         SIZE
dst-k8s-devops-project_fastapi   latest        5f30a3aac8a9   2 minutes ago   1.06GB

# Apres optimisation, reduction de 76% (image slim-buster et build docker multi-stage)
docker image ls

REPOSITORY                       TAG           IMAGE ID       CREATED          SIZE
dst-k8s-devops-project_fastapi   latest        08cbbdd8011d   39 seconds ago   254MB
```

## Publier dans la registry de GitHub

```python
# Initialiser la  variable d'environnement
export CR_TOKEN=<mon_token>

# Se connecter à la registry
echo $CR_TOKEN | docker login ghcr.io -u tiamat-azure --password-stdin

Login Succeeded

# Supprimer l'image en local
docker image rm ghcr.io/tiamat-azure/fast-api:latest

# Verifier
docker image ls

# Builder l'image
docker build -t ghcr.io/tiamat-azure/fast-api:latest .

# Tagger l'image
# docker tag dst-k8s-devops-project_fastapi ghcr.io/tiamat-azure/fast-api:latest

# Publier l'image
docker push ghcr.io/tiamat-azure/fast-api:latest

The push refers to repository [ghcr.io/tiamat-azure/fast-api]
353bcbcbbaa6: Pushed 
1196537dbf35: Pushed 
4b1a65d46545: Pushed 
e567dbffda62: Pushed 
038f8f1ea361: Pushed 
ac3ef569e231: Pushed 
537313a13d90: Pushed 
764055ebc9a7: Pushed 
latest: digest: sha256:6e2927c1461bca55430b13c8126d225109791eea4561b9d3eb6712f67742e871 size: 1997

# Supprimer l'image en local
docker image rm ghcr.io/tiamat-azure/fast-api:latest

# Télécharger l'image
docker pull ghcr.io/tiamat-azure/fast-api:latest

# Vérifier l'image
docker image ls
```
