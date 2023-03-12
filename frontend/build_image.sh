#!/bin/bash

export IMAGE_NAME='froentend'
export IMAGE_TAG='latest'
export LOCAL_CREDENTIAL_PATH='/Users/ivan/.config/gcloud/application_default_credentials.json'

# build dist
# python setup.py sdist

cp "${LOCAL_CREDENTIAL_PATH}" .
# build image
docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .
