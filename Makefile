SHELL=/bin/bash
default: options

options:
	@echo "use one option: run-frontend-local, run-backend-local, run-all-local, pylint-backend, pylint-frontend, run-frontend-local-quiet, run-backend-local-quiet, run-all-local-quiet"

run-frontend-local:
	export SCRIPT_QUIET=FALSE && bash scripts/run-frontend-local.sh

run-backend-local:
	export SCRIPT_QUIET=FALSE && bash scripts/run-backend-local.sh

run-all-local:
	export SCRIPT_QUIET=FALSE && bash scripts/run-all-local.sh

run-frontend-local-quiet:
	export SCRIPT_QUIET=TRUE && bash scripts/run-frontend-local.sh

run-backend-local-quiet:
	export SCRIPT_QUIET=TRUE && bash scripts/run-backend-local.sh

run-all-local-quiet:
	export SCRIPT_QUIET=TRUE && bash scripts/run-all-local.sh

pylint-backend:
	@cd backend && pylint --fail-under=9 main.py model/*.py cfg/*.py util/*.py

pylint-frontend:
	@cd frontend && pylint --fail-under=9 app.py cfg/*.py util/*.py