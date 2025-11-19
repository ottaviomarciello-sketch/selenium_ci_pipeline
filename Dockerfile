# Base image con Python e Jenkins
FROM jenkins/jenkins:lts

# Passa a root per installare pacchetti
USER root

# Aggiorna apt e installa Chromium + dipendenze
RUN apt-get update && \
    apt-get install -y \
        chromium \
        chromium-driver \
        python3-pip \
        python3-venv \
        wget \
        curl \
        unzip \
        gnupg2 \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*

# Imposta Python 3 come default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Installa librerie Python per Selenium
RUN pip install --upgrade pip
RUN pip install selenium webdriver-manager python-dotenv

# Torna all'utente jenkins
USER jenkins

# Porta Jenkins
EXPOSE 8080 50000

# Entrypoint di default
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
