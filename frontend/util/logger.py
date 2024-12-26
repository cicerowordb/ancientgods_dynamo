""" Integrates and initializes all components required for the functionality of this model.
"""

import logging

import cfg

logging.basicConfig(level=cfg.APP_LOG_LEVEL, format=cfg.APP_LOG_FORMAT)

logger = logging.getLogger(__name__)
