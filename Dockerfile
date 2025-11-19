FROM jenkins/jenkins:lts

USER root

# Aggiorna apt e installa dipendenze + Chromium
RUN apt-get update && \
    apt-get install -y \
        chromium \
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

# Torna a utente jenkins
USER jenkins

EXPOSE 8080 50000
