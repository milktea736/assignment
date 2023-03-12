FROM python:3.9

WORKDIR /code

ENV BASE_DIR=/code
ENV PYTHONPATH=${BASE_DIR}/src
ENV PORT=8501
ENV GOOGLE_APPLICATION_CREDENTIALS=${BASE_DIR}/application_default_credentials.json

COPY ./application_default_credentials.json ${GOOGLE_APPLICATION_CREDENTIALS}
COPY ./requirements.txt ${BASE_DIR}/requirements.txt
COPY ./env-build ${BASE_DIR}/.env
COPY ./src ${BASE_DIR}/src

RUN pip install --no-cache-dir --upgrade -r ${BASE_DIR}/requirements.txt

CMD ["sh", "-c", "streamlit run src/frontend/app.py"]
