# Assignment

## Tests and Documents
I wrote some test cases at `backend/tests` and also generate the documents for `backend` project (open `backend/dist/docs/index.html`).

You can also find the RESTful API doc and test it at `https://backend-vd7kas3tda-de.a.run.app/docs`.

## Run services locally

- Set up python environment with requirments.txt.
- Configure the `.env` file in directory.

---

## Create Cloud SQL instance, database and user

Please find the script [here](scripts/init_mysql.sh)

---

## Build frontend and backend service images

Go to `backend` and `frontend` directory then use `docker command` to build or `gcloud builds` to build images.

- docker commands

  ```bash
  cd backend && \
  docker build -t asia.gcr.io/assignment/ivan-backend . && \
  gcloud auth configure-docker && \
  docker push asia.gcr.io/assignment/ivan-backend
  ```

- gcloud commands: `cd frontend && gcloud builds submit --config cloudbuild.yaml .`

Noted. The frontend image can be build on both VM and Cloud Build. But it fails when building backend image, because both VM and Cloud Build memory are insufficient (4G). The building process (pre-download model) exceeds 4G. So I build backend image and push it to container registry.

---

## Deploy `frontend` and `backend` service

My `backend` container consumes more than 4GB memory, so I deploy it to Cloud Run instead of VM.

Pleast find the script [here](scripts/deploy_cloud_run.sh).

- I didn't set the `--min-instances=MIN_INSTANCES`, so it will take some time for cold start if the service has been idle for a long time.
