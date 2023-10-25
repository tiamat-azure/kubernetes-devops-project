# Utiliser une image de base Ubuntu
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Définir les métadonnées de l'image
LABEL org.opencontainers.image.source https://github.com/tiamat-azure/kubernetes-devops-project

# Définir des variables d'environnement
ENV HOME=/home/vscode
ENV BIN=/usr/local/bin
ENV GHRAW=https://raw.githubusercontent.com

# Personnaliser le prompt avec nos dotfiles sur GitHub
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $HOME/.oh-my-zsh/custom/themes/powerlevel10k && \
    wget -O $HOME/.p10k.zsh $GHRAW/tiamat-azure/dotfiles/main/.p10k.zsh && \
    wget -O $HOME/.zshrc $GHRAW/tiamat-azure/dotfiles/main/.zshrc

# Mettre à jour le système et installer les outils de base
# Le positionner en dernier pour mieux exploiter le cache des layers de l'image car sujet a modifications frequentes
RUN apt-get update && \
    apt-get install -y httpie dnsutils figlet && \
    apt-get clean

# Exécuter un shell Zsh au démarrage
ENTRYPOINT ["/bin/zsh"]