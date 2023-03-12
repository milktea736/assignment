#!/bin/bash

#!/bin/bash
export REGION='asia-east1'
export INSTANCE_NAME='ivan-mysql'
export DATABASE_NAME='docs'
export USER_NAME='dev'
export PASSWORD='password'


create_instance(){
    gcloud sql instances create "${INSTANCE_NAME}" \
        --cpu=1 \
        --memory="4GB" \
        --region="${REGION}" \
        --database-version='MYSQL_8_0'
}

create_db(){
    gcloud sql databases create "${DATABASE_NAME}" \
        --instance="${INSTANCE_NAME}"
}

create_sql_user(){
    gcloud sql users create "${USER_NAME}" \
        --host='%' \
        --instance="${INSTANCE_NAME}" \
        --password="${PASSWORD}"
}

create_instance
create_db
create_sql_user
