FROM jenkins/jenkins:lts

USER root

# Install dependencies di sistema
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    wget curl gnupg unzip \
    fonts-liberation libnss3 libx11-xcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
    libxss1 libxtst6 xdg-utils \
    && apt-get clean

# Install Google Chrome stabile
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

USER jenkins

# Assicurati che pip e virtualenv siano aggiornati
RUN python3 -m pip install --upgrade pip virtualenv
