import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'filetolinkbot')
API_ID = int(environ.get('API_ID', '26872474'))
API_HASH = environ.get('API_HASH', 'f8d3a289bf28a13a7159ad0b2ed114e7')
BOT_TOKEN = environ.get('BOT_TOKEN', "5420856904:AAFHQtA3f7A9mn_c034bAPPb7I_af5JD8Eo")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002035856177'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1900118264').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Karnan2k:karnan2k@cluster0.guq8k77.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "techvjautobot")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'gplinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'd3df65a69b586d03f8e861ea6967e9fa608b8444')
