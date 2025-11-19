FROM jenkins/jenkins:lts

USER root

# Install Python + venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl unzip gnupg && \
    apt-get clean

# Install Chromium + dipendenze
RUN apt-get update && \
    apt-get install -y chromium chromium-driver \
        fonts-liberation libnss3 libx11-xcb1 libxcomposite1 libxcursor1 \
        libxdamage1 libxi6 libxtst6 libatk1.0-0 libatk-bridge2.0-0 \
        libdrm2 libxrandr2 libgbm1 libasound2 libpangocairo-1.0-0 \
        libpango-1.0-0 libcups2 libdbus-1-3 libexpat1 libfontconfig1 \
        libfreetype6 libxrender1 libxext6 libxfixes3 libxss1 libglib2.0-0 \
        libjpeg62-turbo libpng16-16 wget && \
    apt-get clean

USER jenkins
