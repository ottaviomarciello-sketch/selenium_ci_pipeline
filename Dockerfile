# Base Jenkins LTS
FROM jenkins/jenkins:lts

USER root

# Imposta non interattivo
ENV DEBIAN_FRONTEND=noninteractive

# Aggiorna e installa Python3, pip, wget, curl, unzip e Chrome
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget curl unzip gnupg2 && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Copia il requirements.txt e installa le dipendenze Python
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Copia i tuoi script nel container
COPY . /app
WORKDIR /app

# Ritorna all'utente jenkins
USER jenkins
