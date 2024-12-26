""" A Flask-based web application to manage and display information about ancient gods.
"""

# pylint: disable=redefined-outer-name
#         - It is acceptable to use generic names like 'err' for exceptions in this context.
# pylint: disable=broad-except
#         - Not all possible exceptions are mapped to maintain simplicity.

from flask import Flask, render_template, request
import requests

import cfg
import util

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static'
)


@app.route('/')
def index():
    """ Display the main page of the application with a list of all gods.
        Retrieves the list from the backend API.
    """
    try:
        response = requests.get(f"{cfg.APP_BACKEND_URL}/list")
        gods = response.json()
    except Exception as err:
        gods = []
        util.logger.error(f"Error connecting to backend: {err}")
    return render_template('index.html', gods=gods)


@app.route('/load')
def load():
    """ 
    """
    return_resp = None
    try:
        response = requests.get(f"{cfg.APP_BACKEND_URL}/load")
        gods = response.json()
        return_resp = render_template(
            'message.html',
            title="Success",
            message="God database loaded!"
        )
    except Exception as err:
        gods = []
        util.logger.error(f"Error connecting to backend: {err}")
        return_resp = render_template(
            'message.html',
            title="Error",
            message="God database not loaded!"
        )
    return return_resp


@app.route('/details/<string:name>')
def details(name):
    """ Display the details of a specific god.
        Fetches the data by the god's name from the backend API.
    """
    try:
        response = requests.get(f"{cfg.APP_BACKEND_URL}/read/{name}")
        god = response.json()
    except Exception as err:
        god = None
        util.logger.error(f"Error connecting to backend: {err}")
    return render_template('details.html', god=god)


@app.route('/add', methods=['GET', 'POST'])
def add_god():
    """ Handle adding a new god to the database.
        On GET: Renders the add form.
        On POST: Sends the form data to the backend API and displays a success or error message.
    """
    return_resp = None
    if request.method == 'POST':
        data = {
            "name": request.form.get('name'),
            "description": request.form.get('description'),
            "greekName": request.form.get('greekName'),
            "romanName": request.form.get('romanName'),
            "category": request.form.get('category'),
            "immortal": request.form.get('immortal'),
            "gender": request.form.get('gender'),
        }
        try:
            response = requests.post(f"{cfg.APP_BACKEND_URL}/add", json=data)
            if response.status_code == 201:
                return_resp = render_template(
                    'message.html',
                    title="Success",
                    message="God added successfully!"
                )
            else:
                return_resp = render_template(
                    'message.html',
                    title="Error",
                    message=response.json().get('error', 'Unknown error.')
                )
        except Exception as err:
            return_resp = render_template(
                'message.html',
                title="Error",
                message=f"Error connecting to backend: {err}"
            )
    else:
        return_resp = render_template('add.html')
    return return_resp


@app.route('/list', methods=['GET'])
def list_ancient_gods():
    """ Retrieve and display a list of all ancient gods from the backend API.
    """
    try:
        response = requests.get(f"{cfg.APP_BACKEND_URL}/list")
        gods = response.json()
    except Exception as err:
        gods = []
        util.logger.error(f"Error connecting to backend: {err}")
    return render_template('list.html', gods=gods)


@app.route('/delete/<string:name>', methods=['GET'])
def delete_ancient_god(name):
    """ Delete a specific ancient god by name from the backend API.
        Displays a success or error message based on the response.
    """
    return_resp = None
    try:
        response = requests.delete(f"{cfg.APP_BACKEND_URL}/delete/{name}")
        if response.status_code == 200:
            return_resp = render_template(
                'message.html',
                title="Success",
                message=f"God '{name}' deleted successfully!"
            )
        else:
            return_resp = render_template(
                'message.html',
                title="Error",
                message=response.json().get('error', 'Unknown error.')
            )
    except Exception as err:
        return_resp = render_template(
            'message.html',
            title="Error",
            message=f"Error connecting to backend: {err}"
        )
    return return_resp


@app.route('/about')
def about():
    """ Display the About page with information about the application.
    """
    return render_template('about.html')


if __name__ == '__main__':
    app.run(
        debug=cfg.APP_DEBUG_MODE,
        host=cfg.APP_IP_ADDRESS,
        port=cfg.APP_TCP_PORT,
        use_reloader=False,
    )
