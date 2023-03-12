FROM python:3.9

WORKDIR /code

ENV BASE_DIR=/code
ENV PYTHONPATH=${BASE_DIR}/src
ENV PORT=80
ENV GOOGLE_APPLICATION_CREDENTIALS=${BASE_DIR}/assignment-ivan-liu.json

COPY ./assignment-ivan-liu.json ${GOOGLE_APPLICATION_CREDENTIALS}
COPY ./requirements.txt ${BASE_DIR}/requirements.txt
# COPY ./.env ${BASE_DIR}/.env
COPY ./env-build ${BASE_DIR}/.env
COPY ./scripts ${BASE_DIR}/scripts
COPY ./scripts/bootstrap.py ${BASE_DIR}/bootstrap.py
COPY ./src ${BASE_DIR}/src

RUN pip install --no-cache-dir --upgrade -r ${BASE_DIR}/requirements.txt
RUN python bootstrap.py

CMD ["sh", "-c", "uvicorn src.backend.main:app --host 0.0.0.0 --port ${PORT}"]
