import os

BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")
USERNAME = os.getenv("DEMOQA_USER", "ottymrc")
PASSWORD = os.getenv("DEMOQA_PASS", "Password.82!")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"