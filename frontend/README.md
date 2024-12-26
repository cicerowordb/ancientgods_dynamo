# Frontend

Install dependencies.

```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-dev python3-venv
python3 -m venv frontenv
source frontenv/bin/activate
pip3 install -r requirements.txt
```

Check code style.

```bash
pylint --fail-under=9 app.py cfg/*.py util/*.py
```

Configure environment.

```bash
export APP_DEBUG_MODE=True
export APP_TCP_PORT=5001
export APP_IP_ADDRESS=0.0.0.0
export APP_LOG_LEVEL=DEBUG
export APP_BACKEND_URL=http://localhost:5000
```

Run application.

```bash
python3 app.py
```

Test manually using browser.

Deactivate Python environment.

```bash
deactivate
```