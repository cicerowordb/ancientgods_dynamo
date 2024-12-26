""" Integrates and initializes all components required for the functionality of this model.
"""

from .dynamodb import get_dynamodb_client
from .logger import logger
from .debug import debug_env_vars
