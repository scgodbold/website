import os

import secret

DEBUG = secret.DEBUG
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Gotta set up dem emails
SNS_TOPIC = secret.SNS_ARN

# Secret key to keep those sessions safe
SECRET_KEY=secret.SECRET_KEY
