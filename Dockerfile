# Étape 1 : Construction de l'environnement
FROM python:3.8.10 as builder

WORKDIR /app
COPY requirements.txt .

# Mettre à jour pip et installer les dépendances dans /build
RUN python -m pip install --upgrade pip==20.0.2
RUN pip install --prefix=/install -r requirements.txt

# Etape finale : livraison
FROM python:3.8.10-slim-buster

# Étape 2 : Image finale
LABEL org.opencontainers.image.source=https://github.com/tiamat-azure/kubernetes-devops-project
LABEL org.opencontainers.image.description="Application FastAPI pour le projet de développement d'applications distribuées et déployables sur Kubernetes."

# Copier les fichiers de l'étape de construction
COPY --from=builder /install /usr/local

WORKDIR /app
COPY . .

# Exposer le port
EXPOSE 5000

# Commande de démarrage
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]