""" Integrates and initializes all components required for the functionality of this model.
"""

import os
from .lang_messages import (
    DEBUG,
    ERROR,
    INFO,
    WARNING
)

APP_DEBUG_MODE = bool(os.getenv('APP_DEBUG_MODE', 'False'))
APP_TCP_PORT = int(os.getenv('APP_TCP_PORT', '5000'))
APP_IP_ADDRESS = (os.getenv('APP_IP_ADDRESS', '127.0.0.1'))
APP_LANG =  os.getenv('APP_LANG', 'pt-br')  # en-us
APP_INITIAL_LIST_JSON =  os.getenv('APP_INITIAL_LIST_JSON', 'all.json')
APP_LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
APP_LOG_LEVEL = os.getenv('APP_LOG_LEVEL', 'INFO').upper()
APP_DYNAMODB_TABLE_NAME = os.getenv('APP_DYNAMO_TABLE_NAME', 'GreekMythology')

DYNAMODB_ENDPOINT_URL = os.getenv('DYNAMODB_ENDPOINT_URL')
AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
