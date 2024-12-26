# Ancient Gods

The Ancient Gods Database is a comprehensive project aimed at cataloging and presenting detailed information about mythological figures from ancient civilizations. This application showcases the fascinating world of mythology, making it accessible to users who wish to explore the stories, attributes, and cultural significance of ancient deities.

Developed as part of the DevOps course by Academia DevOps, this project serves a didactic purpose. It demonstrates the practical application of DevOps principles, including continuous integration, deployment, and infrastructure as code. The goal is to provide students and enthusiasts with a hands-on experience in building, deploying, and managing a real-world application in a DevOps environment.

The application is open for any modifications or extensions, reflecting the collaborative and adaptive spirit of the DevOps culture. Whether you want to add new features, improve functionality, or adapt it to a different mythology, you are encouraged to explore and innovate.

The data for this project, including the list of gods and their attributes, is sourced from the open-source project available at [kamiranoff/greek-mythology-data](https://github.com/kamiranoff/greek-mythology-data/blob/master/package.json). We extend our gratitude to the contributors of this project for providing an invaluable resource that makes this application possible. If any information in this JSON file is incorrect, please contact the responsible party directly, as we have not conducted any evaluation of the content of the data.

## How to run locally

This is a Python 3 application. It uses Flask and Jinja2 for the frontend and Flask with DynamoDB for the backend. A Docker container is used to run DynamoDB locally.


### Prerequisites

To run this application locally, you will need the following:
- Docker
- Python 3
- Python 3-pip
- Python 3-venv
- Pylint (optional, for code style checks)

The `make` command provides the following options for managing the application:

```bash
make
```

<code>use one option: run-frontend-local, run-backend-local, run-all-local, pylint-backend, pylint-frontend, run-frontend-local-quiet, run-backend-local-quiet, run-all-local-quiet</code>

Available options:
- `run-frontend-local`: Run the frontend locally.
- `run-backend-local`: Run the backend locally.
- `run-all-local`: Run both frontend and backend locally.
- `pylint-backend`: Check code style for the backend.
- `pylint-frontend`: Check code style for the frontend.
- `run-frontend-local-quiet`: Run the frontend locally with minimal logs.
- `run-backend-local-quiet`: Run the backend locally with minimal logs.
- `run-all-local-quiet`: Run both frontend and backend locally with minimal logs.

To run the entire application locally with verbosity, use the following command. Note that it uses TCP ports 5000 and 5001:

```bash
make run-all-local
```

To run the application with minimal logs, use:

```bash
make run-all-local-quiet
```

## How to check

To check the backend code style:

```bash
make pylint-backend
```

The output will indicate the code rating. Example:

<code>--------------------------------------------------------------------<br>
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)</code>


To check the frontend code style:

```bash
make pylint-frontend
```

The output will indicate the code rating. Example:

<code>--------------------------------------------------------------------<br>
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)</code>

## Known issues and future work

- When attempting to remove a non-existent entity, the code gives positive feedback instead of an error message. Only a message issue.
- A script to build the Docker image is needed for easier deployment.
- Unit tests are currently missing and need to be implemented.
- Integration tests are also required to ensure system-wide functionality.
- Only backend is adapt for English and Portuguse.
