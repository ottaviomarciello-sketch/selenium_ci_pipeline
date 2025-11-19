# Base Jenkins LTS
FROM jenkins/jenkins:lts

USER root

# Aggiornamento e installazione pacchetti necessari
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    unzip \
    gnupg \
    curl \
    software-properties-common \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    lsb-release \
    xdg-utils \
    && apt-get clean

# Installazione di Google Chrome stabile
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Impostazioni ambiente
ENV PATH="/usr/local/bin:$PATH"

# Impostazione utente Jenkins
USER jenkins

# Directory di lavoro
WORKDIR /var/jenkins_home

# Copia eventuale requirements.txt nella build
COPY requirements.txt .

# Installazione Python packages (anche webdriver-manager)
RUN python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Comando di default
CMD ["jenkins"]
