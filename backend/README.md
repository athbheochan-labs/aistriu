# Aistriu Backend

FastAPI backend for Aistriu.

## Requirements

- Python 3.11+

## Local Development

From the `backend` directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
fastapi dev app/main.py
```

The API will be available at `http://127.0.0.1:8000`.

Useful endpoints:

- Health check: `GET /health`
- Swagger docs: `GET /docs`
- OpenAPI schema: `GET /openapi.json`

## Configuration

Configuration is loaded from environment variables and an optional `.env` file using `pydantic-settings`.

| Variable | Default | Description |
| --- | --- | --- |
| `APP_NAME` | `Aistriu API` | FastAPI application title. |
| `APP_ENV` | `local` | Runtime environment name. |
| `APP_DEBUG` | `false` | Enables debug mode in FastAPI. |
| `CORS_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | Comma-separated allowed origins for the SvelteKit frontend. |
| `VALKEY_URL` | unset | Optional Valkey connection URL. |

## Docker

The root `compose.yml` runs the backend with Valkey for local development:

```bash
cd ..
cp .env.example .env
docker compose up --build
```

## Render

The production Docker entrypoint is configured in `backend/Dockerfile`. Render deployment is managed from the root `render.yaml` Blueprint.

## Project Structure

```text
backend/
  app/
    api/
      routes/
        health.py
      router.py
    core/
      config.py
    main.py
  .env.example
  pyproject.toml
  README.md
```
