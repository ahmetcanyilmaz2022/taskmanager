# Task Manager

A small Task Manager API built with FastAPI + SQLModel (SQLite).
Dockerized and ready to run locally with `docker-compose` or as a single Docker image. Basic Kubernetes manifests included.

## Quickstart (Docker)

Build:

```bash
docker build -t yourname/task-manager:latest .
```

Run:

```bash
docker run -p 8000:8000 yourname/task-manager:latest
```

Open `http://localhost:8000/docs` to see OpenAPI / Swagger UI.

## Quickstart (docker-compose)

```bash
docker-compose up --build
```

## Kubernetes

1. Push your image to a registry: `docker push yourname/task-manager:latest`
2. Apply manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Then access via NodePort on your node port (30080).

## Notes

* DB is SQLite file (`app.db`). For production, switch to Postgres / managed RDS and update DATABASE_URL accordingly.
* You can extend with authentication, migrations (alembic), CI/CD pipeline (GitHub Actions) and more.
