# Render Deployment

This project deploys the SvelteKit frontend and FastAPI backend to Render using the root `render.yaml` Blueprint.

## Services

The Blueprint defines two free Render services:

- `aistriu-frontend`: SvelteKit static site at `aistriu.athbheochan.irish`
- `aistriu-backend`: FastAPI Docker web service at `api.aistriu.athbheochan.irish`

## Frontend

- Name: `aistriu-frontend`
- Runtime: Static site
- Build command: `cd frontend && npm ci && npm run build`
- Publish path: `frontend/build`
- Custom domain: `aistriu.athbheochan.irish`

The frontend is built as a static SvelteKit site:

```bash
cd frontend && npm ci && npm run build
```

Render publishes the generated `frontend/build` directory.

## Backend

- Name: `aistriu-backend`
- Runtime: Docker
- Dockerfile: `backend/Dockerfile`
- Health check: `/health`
- Custom domain: `api.aistriu.athbheochan.irish`

The backend container starts with:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

Render provides `PORT` at runtime. Locally, the container falls back to `8000`.

## Environment Variables

Managed in Render from the Blueprint and service dashboard:

| Variable | Value | Notes |
| --- | --- | --- |
| `APP_NAME` | `Aistriu API` | Set in `render.yaml`. |
| `APP_ENV` | `production` | Set in `render.yaml`. |
| `APP_DEBUG` | `false` | Set in `render.yaml`. |
| `CORS_ORIGINS` | `https://aistriu.athbheochan.irish` | Set in `render.yaml`. |
| `VALKEY_URL` | dashboard-managed | Leave unset until a hosted Valkey/Redis-compatible service is added. |
| `PUBLIC_API_BASE_URL` | `https://api.aistriu.athbheochan.irish` | Set on the frontend service in `render.yaml`. |

Values marked `sync: false` in `render.yaml` are intentionally managed in the Render dashboard and are not synced from git.

## Deploy

1. Create a new Render Blueprint from this GitHub repository.
2. Render will detect `render.yaml` in the repository root.
3. Confirm the `aistriu-frontend` and `aistriu-backend` services.
4. Set dashboard-managed env vars when prompted.
5. Deploy.

## DNS

After the Render services exist, add both custom domains in Render:

- `aistriu.athbheochan.irish` on the frontend static site
- `api.aistriu.athbheochan.irish` on the backend web service

In Route 53, create a record in the `athbheochan.irish` hosted zone:

| Field | Value |
| --- | --- |
| Record name | `aistriu` |
| Record type | `CNAME` |
| Value | Render's custom-domain target for the frontend service |
| TTL | `300` |

Create a second record:

| Field | Value |
| --- | --- |
| Record name | `api.aistriu` |
| Record type | `CNAME` |
| Value | Render's custom-domain target for the backend service |
| TTL | `300` |

Render shows each exact CNAME target in the corresponding service's custom domain screen. After DNS propagates, Render provisions and renews TLS automatically.
