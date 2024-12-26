""" Module Docstring
"""

# disable pylint warnings
# pylint: disable=redefined-outer-name
#          - it is absurd give a different name for each error variable.
# pylint: disable=broad-except
#          - not all possible exceptions were mapped.

import json

from flask import Flask, request, jsonify

import cfg
import util
import model


app = Flask(__name__)

dynamodb = util.get_dynamodb_client()
table = dynamodb.Table(cfg.APP_DYNAMODB_TABLE_NAME)

def load_data_to_dynamo(file_name):
    """
    Represents an ancient god with various attributes.
    Attributes:
        name (str): The name of the god.
        greek_name (str): The Greek equivalent name (optional).
        roman_name (str): The Roman equivalent name (optional).
        category (str): The category or type of god (optional).
        description (str): A description of the god.
        immortal (bool): Whether the god is immortal (optional).
        gender (str): Gender of the god (optional).
        images (dict): A dictionary of image references (optional).
        relatives (dict): A dictionary of relatives (optional).
        books (list): A list of books associated with the god (optional).
        events (list): A list of events associated with the god (optional).
    """
    util.logger.debug(cfg.DEBUG[cfg.APP_LANG]['start_loading_data'])

    with open(file_name, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)

    for item in data:
        god = model.AncientGod(
            name=item.get('name'),
            description=item.get('description'),
            attributes={
                "greek_name": item.get('greekName'),
                "roman_name": item.get('romanName'),
                "category": item.get('category'),
                "immortal": item.get('immortal'),
                "gender": item.get('gender'),
                "images": item.get('images'),
                "relatives": item.get('relatives'),
                "books": item.get('books'),
                "events": item.get('events')
            }
        )
        table.put_item(Item=god.json())
        util.logger.info(cfg.INFO[cfg.APP_LANG]['item_inserted'].format(name=god.name))

@app.route('/add', methods=['POST'])
def add_ancient_god():
    """
    Add a new ancient god to the DynamoDB table.
    Returns:
        Response: A Flask response with a success or error message.
    """
    util.logger.debug(cfg.DEBUG[cfg.APP_LANG]['add_request_received'])
    data = request.json
    if not data.get('name') or not data.get('description'):
        util.logger.warning(cfg.WARNING[cfg.APP_LANG]['missing_required_fields'])
        return (
            jsonify({'error': cfg.WARNING[cfg.APP_LANG]['missing_required_fields']})
            , 400
        )

    god = model.AncientGod(
        name=data.get('name'),
        description=data.get('description'),
        attributes={
            "greek_name": data.get('greekName'),
            "roman_name": data.get('romanName'),
            "category": data.get('category'),
            "immortal": data.get('immortal'),
            "gender": data.get('gender'),
            "images": data.get('images'),
            "relatives": data.get('relatives'),
            "books": data.get('books'),
            "events": data.get('events')
        }
    )
    try:
        table.put_item(Item=god.json())
        util.logger.info(cfg.INFO[cfg.APP_LANG]['god_added'].format(name=god.name))
        return (
            jsonify({'message': cfg.INFO[cfg.APP_LANG]['god_added'].format(name=god.name)}),
            201
        )
    except Exception as err:
        util.logger.error(cfg.ERROR[cfg.APP_LANG]['add_god_error'].format(err=str(err)))
        return (
            jsonify({'error': cfg.ERROR[cfg.APP_LANG]['add_god_error'].format(err=str(err))}),
            500
        )

@app.route('/list', methods=['GET'])
def list_ancient_gods():
    """
    Retrieve and return a list of all ancient gods from the DynamoDB table.
    Returns:
        Response: A Flask response with the list of gods or an error message.
    """
    util.logger.debug(cfg.DEBUG[cfg.APP_LANG]['list_request_received'])
    try:
        response = table.scan()
        items = response.get('Items', [])
        util.logger.info(cfg.INFO[cfg.APP_LANG]['list_items_count'].format(count=len(items)))
        return jsonify(items), 200
    except Exception as err:
        util.logger.error(cfg.ERROR[cfg.APP_LANG]['list_gods_error'].format(err=str(err)))
        return (
            jsonify({'error': cfg.ERROR[cfg.APP_LANG]['list_gods_error'].format(err=str(err))}),
            500
        )

@app.route('/read/<string:name>', methods=['GET'])
def read_ancient_god(name):
    """
    Fetch and return details of a specific ancient god by name from the DynamoDB table.
    Args:
        name (str): The name of the god to fetch.
    Returns:
        Response: A Flask response with the god details or an error message.
    """
    util.logger.debug(cfg.DEBUG[cfg.APP_LANG]['read_request_received'].format(name=name))
    return_resp = None
    try:
        response = table.get_item(Key={'name': name})
        item = response.get('Item')
        if item:
            util.logger.info(cfg.INFO[cfg.APP_LANG]['god_fetched'].format(name=name))
            return_resp = jsonify(item), 200
        else:
            util.logger.warning(cfg.WARNING[cfg.APP_LANG]['god_not_found'].format(name=name))
            return_resp = (
                jsonify({'error': cfg.WARNING[cfg.APP_LANG]['god_not_found'].format(name=name)}),
                404
            )
    except Exception as err:
        util.logger.error(cfg.ERROR[cfg.APP_LANG]['read_god_error'].format(err=str(err)))
        return_resp = (
            jsonify({'error': cfg.ERROR[cfg.APP_LANG]['read_god_error'].format(err=str(err))}),
            500
        )
    return return_resp

@app.route('/delete/<string:name>', methods=['DELETE'])
def delete_ancient_god(name):
    """
    Delete a specific ancient god by name from the DynamoDB table.
    Args:
        name (str): The name of the god to delete.
    Returns:
        Response: A Flask response with a success or error message.
    """
    util.logger.debug(cfg.DEBUG[cfg.APP_LANG]['delete_request_received'].format(name=name))
    return_resp = None
    try:
        table.delete_item(
            Key={'name': name}
        )
        util.logger.info(cfg.INFO[cfg.APP_LANG]['god_removed'].format(name=name))
        return_resp = (
            jsonify({'message': cfg.INFO[cfg.APP_LANG]['god_removed'].format(name=name)}),
            200
        )
    except Exception as err:
        util.logger.error(cfg.ERROR[cfg.APP_LANG]['delete_god_error'].format(err=str(err)))
        return_resp = (
            jsonify({'error': cfg.ERROR[cfg.APP_LANG]['delete_god_error'].format(err=str(err))}),
            500
        )
    return return_resp

@app.route('/load', methods=['GET'])
def load_data():
    """ 
    """
    return_resp = None
    try:
        util.logger.debug(cfg.DEBUG[cfg.APP_LANG]['start_loading_data'])
        load_data_to_dynamo(cfg.APP_INITIAL_LIST_JSON)
        util.logger.info(cfg.INFO[cfg.APP_LANG]['json_data_loaded'])
        return_resp = (
            jsonify({'message': f'loaded {cfg.APP_INITIAL_LIST_JSON}'}),
            200
        )
    except Exception as err:
        util.logger.error(cfg.ERROR[cfg.APP_LANG]['json_load_error'].format(err=str(err)))
        return_resp = (
            jsonify({'message': f'ERROR: {err}'}),
            200
        )
    return return_resp


if __name__ == '__main__':
    util.debug_env_vars()
    util.logger.debug(cfg.DEBUG[cfg.APP_LANG]['app_start'])
    app.run(
        debug=cfg.APP_DEBUG_MODE,
        host=cfg.APP_IP_ADDRESS,
        port=cfg.APP_TCP_PORT,
    )
