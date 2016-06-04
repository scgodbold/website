import os

import secret

DEBUG = secret.DEBUG
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Gotta set up dem emails
SNS_TOPIC = secret.SNS_ARN

# Secret key to keep those sessions safe
SECRET_KEY = secret.SECRET_KEY

# Groupmebots config
GROUPME_BOT_VERSION = '3.0.0'
GROUPME_URL = 'https://api.groupme.com/v3/bots/post'
GROUPME_BOTS = secret.GROUPME_BOTS  # This is a dictionary with GroupID: BotID pairs

# Imgur API
IMGUR_URL = 'https://api.imgur.com/3/'
IMGUR_CLIENT_ID = secret.IMGUR_CLIENT_ID
