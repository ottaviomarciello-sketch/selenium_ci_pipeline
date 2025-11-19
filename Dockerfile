# Base image: Debian slim per minor peso
FROM python:3.13-slim

# Aggiorna pacchetti e installa dipendenze necessarie per Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libgtk-3-0 \
    libxss1 \
    libappindicator3-1 \
    xdg-utils \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Installa Chrome stabile
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Imposta variabili d'ambiente per Chrome
ENV CHROME_BIN=/usr/bin/google-chrome
ENV PATH="$PATH:/usr/local/bin"

# Installa pip e Selenium dependencies
WORKDIR /app
COPY requirements.txt .
RUN python -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Copia il codice Python
COPY . .

# Comando di default (puoi sostituire con il tuo script)
CMD ["/bin/bash"]
