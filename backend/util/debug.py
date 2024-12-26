""" Module providing debugging routines for application configuration.
    Includes functions to log the values and types of key environment variables,
    enabling better visibility into the application's configuration state for troubleshooting.
"""

import util.logger
import cfg

def debug_env_vars():
    """
    Log environment variable values and their types for debugging purposes.

    This function outputs the current state of key configuration variables used in the application,
    helping to identify issues with the environment setup.
    """
    util.logger.debug('================%s======================',
                 __name__)
    util.logger.debug('APP_DEBUG_MODE: %s %s',
                 cfg.APP_DEBUG_MODE,
                 type(cfg.APP_DEBUG_MODE))
    util.logger.debug('APP_LANG: %s %s',
                 {cfg.APP_LANG},
                 {type(cfg.APP_LANG)})
    util.logger.debug('APP_INITIAL_LIST_JSON: %s %s',
                 {cfg.APP_INITIAL_LIST_JSON},
                 {type(cfg.APP_INITIAL_LIST_JSON)})
    util.logger.debug('APP_LOG_FORMAT: %s %s',
                 {cfg.APP_LOG_FORMAT},
                 {type(cfg.APP_LOG_FORMAT)})
    util.logger.debug('APP_LOG_LEVEL: %s %s',
                 {cfg.APP_LOG_LEVEL},
                 {type(cfg.APP_LOG_LEVEL)})
    util.logger.debug('APP_DYNAMODB_TABLE_NAME: %s %s',
                 {cfg.APP_DYNAMODB_TABLE_NAME},
                 {type(cfg.APP_DYNAMODB_TABLE_NAME)})
    util.logger.debug('DYNAMODB_ENDPOINT_URL: %s %s',
                 {cfg.DYNAMODB_ENDPOINT_URL},
                 {type(cfg.DYNAMODB_ENDPOINT_URL)})
    util.logger.debug('AWS_REGION: %s %s',
                 {cfg.AWS_REGION},
                 {type(cfg.AWS_REGION)})
    util.logger.debug('AWS_ACCESS_KEY_ID: %s %s',
                 {cfg.AWS_ACCESS_KEY_ID},
                 {type(cfg.AWS_ACCESS_KEY_ID)})
    util.logger.debug('AWS_SECRET_ACCESS_KEY: %s %s',
                 {cfg.AWS_SECRET_ACCESS_KEY},
                 {type(cfg.AWS_SECRET_ACCESS_KEY)})
    util.logger.debug('================%s======================',
                 __name__)
