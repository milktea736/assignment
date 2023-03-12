#!/bin/bash

export IMAGE_NAME='backend'
export IMAGE_TAG='latest'
export LOCAL_CREDENTIAL_PATH=''

# build dist
# python setup.py sdist

cp "${LOCAL_CREDENTIAL_PATH}" .
# build image
docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .
