#!/bin/bash

echo "✅ Running frontend and backend"

cleanup() {
    echo "✅ Finishing scripts"
    kill 0
}

trap cleanup SIGINT

bash scripts/run-frontend-local.sh &
bash scripts/run-backend-local.sh &

echo "⌛ Starting applications..."
echo "👉 Press Ctrl+c to finish all"

wait
