#!/bin/bash

export REGION='asia-east1'
export FROTEND_SERVICE_NAME='frontend'
export BACKEND_SERVICE_NAME='backend'

gcloud run services delete "${FROTEND_SERVICE_NAME}" --region "${REGION}"
gcloud run services delete "${BACKEND_SERVICE_NAME}" --region "${REGION}"