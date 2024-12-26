""" Module for interacting with DynamoDB.
    Provides functions and utilities for creating a DynamoDB client using
    the application's configuration settings.
"""
import boto3

import cfg

def get_dynamodb_client():
    """
    Create and return a DynamoDB client using the configured credentials and settings.

    Returns:
        boto3.resources.base.ServiceResource: A DynamoDB service resource object.
    """
    return boto3.resource(
        'dynamodb',
        endpoint_url=cfg.DYNAMODB_ENDPOINT_URL,
        region_name=cfg.AWS_REGION,
        aws_access_key_id=cfg.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=cfg.AWS_SECRET_ACCESS_KEY
    )
