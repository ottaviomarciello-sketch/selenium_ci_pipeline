FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install Chrome ARM64
RUN apt-get update && \
    apt-get install -y wget gnupg2 curl unzip && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=arm64] http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Copy deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Add project
COPY . /app
WORKDIR /app

CMD ["python", "script.py"]
