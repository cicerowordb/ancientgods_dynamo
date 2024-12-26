#!/bin/bash

echo "✅ Running backend"

if test "$SCRIPT_QUIET " = "TRUE "
then
    REDIRECTION="/dev/null"
else
    REDIRECTION="&1"
fi

if (! which docker > /dev/null && test "$CREATE_DYNAMODB_TABLE " = "TRUE ")
then
    echo "⛔ The 'docker' command is required"
fi

if ! which aws > /dev/null
then
    echo "⛔ The 'aws' command is required"
fi

if ! which python3 > /dev/null
then
    echo "⛔ The 'python3' command is required"
fi

if ! which pip3 > /dev/null
then
    echo "⛔ The 'pip3' command is required"
fi

if ! python3 -m venv --help > /dev/null
then
    echo "⛔ The 'venv' module for Python is required"
fi

cd ./backend

python3 -m venv backenv >$REDIRECTION 2>$REDIRECTION
source backenv/bin/activate >$REDIRECTION 2>$REDIRECTION
pip3 install -r requirements.txt -q >$REDIRECTION 2>$REDIRECTION

export DYNAMODB_ENDPOINT_URL=${DYNAMODB_ENDPOINT_URL:-http://localhost:8000}
export AWS_REGION=${AWS_REGION:-us-west-2}
export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID:-fakeAccessKeyId}
export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY:-fakeSecretAccessKey}
export APP_DYNAMODB_TABLE_NAME=${APP_DYNAMODB_TABLE_NAME:-GreekMythology}
export CREATE_DYNAMODB_TABLE=${CREATE_DYNAMODB_TABLE:-TRUE}

if test $CREATE_DYNAMODB_TABLE = TRUE
then

    docker run --rm -d -p 8000:8000 --name dynamodb --rm amazon/dynamodb-local

    aws dynamodb create-table --endpoint-url $DYNAMODB_ENDPOINT_URL --region $AWS_REGION \
        --table-name $APP_DYNAMODB_TABLE_NAME \
        --attribute-definitions AttributeName=name,AttributeType=S \
        --key-schema AttributeName=name,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
        --tags Key=Owner,Value=AcadDevOps
fi

export APP_TCP_PORT=${APP_TCP_PORT:-5000}
export APP_IP_ADDRESS=${APP_IP_ADDRESS:-0.0.0.0}
export APP_LANG=${APP_LANG:-pt-br}
# export APP_INITIAL_LIST_JSON

if test $SCRIPT_QUIET = TRUE
then 
    export APP_LOG_LEVEL=INFO
    export APP_DEBUG_MODE=False
else
    export APP_LOG_LEVEL=DEBUG
    export APP_DEBUG_MODE=True
fi

python3 main.py
