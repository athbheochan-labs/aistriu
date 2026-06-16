# Aistriu

Local development setup for the Aistriu FastAPI backend, SvelteKit frontend, and supporting services.

## Docker Compose

Copy the example environment file:

```bash
cp .env.example .env
```

Start the frontend, backend, and Valkey:

```bash
docker compose up --build
```

The SvelteKit frontend will be available at `http://127.0.0.1:5173`.

The FastAPI backend will be available at `http://127.0.0.1:8000`.

Useful endpoints:

- Health check: `GET /health`
- Swagger docs: `GET /docs`

Test the health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

Valkey is available to the backend at `redis://valkey:6379/0`. From the host machine, it is exposed at `redis://localhost:6379/0` by default.

## Services

| Service | Description | Default URL |
| --- | --- | --- |
| `frontend` | SvelteKit dev server | `http://127.0.0.1:5173` |
| `backend` | FastAPI API server | `http://127.0.0.1:8000` |
| `valkey` | Valkey cache service | `redis://localhost:6379/0` |

## Environment Variables

Compose reads configuration from the root `.env` file.

| Variable | Default | Description |
| --- | --- | --- |
| `APP_NAME` | `Aistriu API` | FastAPI application title. |
| `APP_ENV` | `local` | Runtime environment name. |
| `APP_DEBUG` | `true` | Enables debug mode in local development. |
| `CORS_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | Comma-separated allowed origins for the SvelteKit frontend. |
| `BACKEND_PORT` | `8000` | Host port for the FastAPI service. |
| `FRONTEND_PORT` | `5173` | Host port for the SvelteKit dev server. |
| `VALKEY_PORT` | `6379` | Host port for Valkey. |
| `VALKEY_URL` | `redis://valkey:6379/0` | Valkey connection URL used inside Compose. |
| `PUBLIC_API_BASE_URL` | `http://localhost:8000` | Browser-facing URL for the FastAPI backend. |

## Deployment

The SvelteKit frontend and FastAPI backend are configured for Render using the root `render.yaml` Blueprint.

Deployment notes, environment variables, and Route 53 DNS steps are documented in `docs/deployment/render.md`.
