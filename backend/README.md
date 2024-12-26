# Backend

Install dependencies.

```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-dev python3-venv
python3 -m venv backenv
source backenv/bin/activate
pip3 install -r requirements.txt
```

Run DynamoDB locally.

```bash
docker run -d -p 8000:8000 --name dynamodb --rm amazon/dynamodb-local
```

Prepare DynamoDB table.

```bash
export DYNAMODB_ENDPOINT_URL=http://localhost:8000
export AWS_REGION=us-west-2
export AWS_ACCESS_KEY_ID=fakeAccessKeyId
export AWS_SECRET_ACCESS_KEY=fakeSecretAccessKey
export APP_DYNAMODB_TABLE_NAME=GreekMythology

aws dynamodb list-tables --endpoint-url $DYNAMODB_ENDPOINT_URL --region $AWS_REGION
aws dynamodb create-table --endpoint-url $DYNAMODB_ENDPOINT_URL --region $AWS_REGION \
    --table-name $APP_DYNAMODB_TABLE_NAME \
    --attribute-definitions AttributeName=name,AttributeType=S \
    --key-schema AttributeName=name,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --tags Key=Owner,Value=AcadDevOps
aws dynamodb list-tables --endpoint-url $DYNAMODB_ENDPOINT_URL --region $AWS_REGION
aws dynamodb scan --endpoint-url $DYNAMODB_ENDPOINT_URL --region $AWS_REGION \
    --table-name $APP_DYNAMODB_TABLE_NAME
```

Check code style.

```bash
pylint --fail-under=9 main.py model/*.py cfg/*.py util/*.py
```

Configure environment.

```bash
export APP_DEBUG_MODE=True
export APP_TCP_PORT=5000
export APP_IP_ADDRESS=0.0.0.0
export APP_LANG=pt-br
# export APP_INITIAL_LIST_JSON
export APP_LOG_LEVEL=DEBUG
```

Run application.

```bash
python3 main.py
```

Test application.

```bash
curl -X GET http://127.0.0.1:5000/list
curl -X POST http://127.0.0.1:5000/add \
-H "Content-Type: application/json" \
-d '{
    "name": "Zeus",
    "description": "God of the sky and thunder.",
    "greekName": "Zeus",
    "romanName": "Jupiter",
    "category": "Olympian",
    "immortal": true,
    "gender": "Male"
}'
curl -X GET http://127.0.0.1:5000/list|less
curl -X GET http://127.0.0.1:5000/read/Zeus
curl -X DELETE http://127.0.0.1:5000/delete/Zeus
 ```


```bash
curl -X GET http://127.0.0.1:5000/read/DoNotExist
curl -X DELETE http://127.0.0.1:5000/delete/DoNotExist
 ```


Delete DynamoDB container and deactivate Python environment.

```bash
docker rm dynamodb
deactivate
```
