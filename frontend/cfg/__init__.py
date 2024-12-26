""" Configuration module for the Flask application.
    Defines environment variables and default settings.
"""

import os

APP_DEBUG_MODE = bool(os.getenv('APP_DEBUG_MODE', 'False'))
APP_TCP_PORT = int(os.getenv('APP_TCP_PORT', '5001'))
APP_IP_ADDRESS = os.getenv('APP_IP_ADDRESS', '127.0.0.1')
APP_LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
APP_LOG_LEVEL = os.getenv('APP_LOG_LEVEL', 'INFO').upper()
APP_BACKEND_URL = os.getenv('APP_BACKEND_URL', 'http://localhost:5000')
