#!/bin/bash
echo "✅ Running frontend"

if test "$SCRIPT_QUIET " = "TRUE "
then
    REDIRECTION="/dev/null"
else
    REDIRECTION="&1"
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

cd ./frontend

python3 -m venv frontenv >$REDIRECTION 2>$REDIRECTION
source frontenv/bin/activate >$REDIRECTION 2>$REDIRECTION
pip3 install -r requirements.txt -q  >$REDIRECTION 2>$REDIRECTION

export APP_TCP_PORT=${APP_TCP_PORT:-5001}
export APP_IP_ADDRESS=${APP_IP_ADDRESS=0.0.0.0}
export APP_BACKEND_URL=${APP_BACKEND_URL:-http://localhost:5000}
if test $SCRIPT_QUIET = TRUE
then 
    export APP_LOG_LEVEL=INFO
    export APP_DEBUG_MODE=False
else
    export APP_LOG_LEVEL=DEBUG
    export APP_DEBUG_MODE=True
fi

python3 app.py
