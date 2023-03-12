#!/bin/bash

export FROTEND_PORT=8501
export BACKEND_PORT=80
export REGION='asia-east1'
export MAX_INSTANCES=1
export FROTEND_SERVICE_NAME='frontend'
export BACKEND_SERVICE_NAME='backend'
export FROTEND_IMAGE='asia.gcr.io/assignment/ivan-frontend'
export BACKEND_IMAGE='asia.gcr.io/assignment/ivan-backend'

# find the backend url then fill
export SERVICE_HOST='https://backend-vd7kas3tda-de.a.run.app'

deploy_frontend(){
    gcloud run deploy "${FROTEND_SERVICE_NAME}" \
        --image "${FROTEND_IMAGE}" \
        --port "${FROTEND_PORT}"  --region "${REGION}" \
        --set-env-vars SERVICE_HOST="${SERVICE_HOST}" \
        --ingress all \
        --allow-unauthenticated
}

deploy_backend(){
    gcloud run deploy "${BACKEND_SERVICE_NAME}" \
        --image "${BACKEND_IMAGE}" \
        --cpu 2 \
        --port "${BACKEND_PORT}"  --region "${REGION}" \
        --memory '6Gi' \
        --ingress all \
        --allow-unauthenticated
}

deploy_backend
deploy_frontend