# FastAPI Docker Demo

A simple REST API built with FastAPI and Python, fully containerized with Docker.

---

## What This Project Does

This is a lightweight API that lets you:
- Check if the service is running (`/health`)
- Store and retrieve items (`/items`)
- View interactive API docs automatically at `/docs`

---

## Requirements

Before you start, make sure you have these installed:

| Tool | Download |
|------|----------|
| Docker Desktop | https://www.docker.com/products/docker-desktop |
| Git (optional) | https://git-scm.com |

That's it. You do not need Python installed on your machine.

---

## Project Structure

```
fast-api-docker/
├── main.py              # The API application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Instructions to build the container
├── .dockerignore        # Files to exclude from the build
├── docker-compose.yml   # Easy way to run the app
└── README.md            # This file
```

---

## How To Run

### Option 1 — Docker Compose (recommended)

```bash
docker compose up --build
```

Then open your browser and go to:
- API: http://localhost:8000
- Health check: http://localhost:8000/health
- Interactive docs: http://localhost:8000/docs

To stop it:
```bash
docker compose down
```

---

### Option 2 — Run on a different port

```bash
PORT=9000 docker compose up --build
```

Then visit http://localhost:9000

---

### Option 3 — Plain Docker (without Compose)

```bash
# Build the image
docker build -t myapi .

# Run on port 8000
docker run -p 8000:8000 myapi

# Run on a different port
docker run -p 9000:8000 -e PORT=8000 myapi
```

---

## API Endpoints

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| GET    | `/`       | Welcome message          |
| GET    | `/health` | Health check — returns `{"status": "ok"}` |
| GET    | `/items`  | List all items           |
| POST   | `/items`  | Create a new item        |

### Example — create an item

```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Apple", "description": "A red apple"}'
```

Response:
```json
{"id": 1, "name": "Apple", "description": "A red apple"}
```

---

## Health Check

Docker automatically monitors the `/health` endpoint every 30 seconds.
If the app stops responding, Docker will restart it automatically.

You can check the health status manually:
```bash
docker ps
```

Look for the `STATUS` column — it will show `healthy` when everything is running correctly.

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT`   | `8000`  | The port the API runs on |

---

## Stopping the App

```bash
# If using Compose
docker compose down

# If using plain Docker
docker stop <container_id>
```

---

## Troubleshooting

**Port already in use?**
Change the port: `PORT=9000 docker compose up --build`

**Docker not running?**
Open Docker Desktop and wait for it to fully start, then try again.

**Want to see logs?**
```bash
docker compose logs -f
```