import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
MONGO_URIS = os.getenv("MONGO_URIS").split(",")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
DATABASE_CHANNELS = list(map(int, os.getenv("DATABASE_CHANNELS").split(",")))
ADMINS = list(map(int, os.getenv("ADMINS").split(",")))
FSUB_CHANNELS = list(map(int, os.getenv("FORCE_SUB_CHANNELS").split(",")))
FSUB_MODE = os.getenv("FSUB_MODE", "off").lower() == "on"
IMDB_API_KEY = os.getenv("IMDB_API_KEY")
PREMIUM_PLAN = os.getenv("PREMIUM_PLAN", "False") == "True"
REFERRAL_MODE = os.getenv("REFERRAL_MODE", "False") == "True"
URL_SHORTENER_MODE = os.getenv("URL_SHORTENER_MODE", "False") == "True"
AUTO_APPROVE = os.getenv("AUTO_APPROVE", "False") == "True"
AUTO_DELETE = os.getenv("AUTO_DELETE", "False") == "True"
LANGUAGE_FILTER = os.getenv("LANGUAGE_FILTER", "False") == "True"
GOOD_WISHES = os.getenv("GOOD_WISHES", "False") == "True"
SPAM_FILTER = os.getenv("SPAM_FILTER", "False") == "True"

# Shortener websites config
SHORTENER_SERVICES = []
SHORTENER_KEYS = os.getenv("SHORTENER_KEYS")
if SHORTENER_KEYS:
    for service in SHORTENER_KEYS.split("|"):  # Format: name,domain,apikey,verify
        try:
            name, domain, apikey, verify = service.split(",")
            SHORTENER_SERVICES.append({
                "name": name,
                "domain": domain,
                "apikey": apikey,
                "verify": verify.lower() == "true"
            })
        except ValueError:
            continue
