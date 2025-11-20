FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Installa dipendenze + Chromium + Chromedriver per ARM64
RUN apt-get update && \
    apt-get install -y wget curl unzip gnupg2 chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# Copia requirements e installa pacchetti Python
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia progetto
COPY . /app
WORKDIR /app

CMD ["python3", "wikipedia_python.py"]
