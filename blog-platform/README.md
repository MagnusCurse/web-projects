## Blog Platform – Getting Started

This repository contains a Spring Boot backend, a React (Vite + TypeScript) frontend, and a Dockerized PostgreSQL database.

### Prerequisites

- Java 21 (for Spring Boot)
- Node.js 18+ and npm (for Vite)
- Docker Desktop running (for PostgreSQL + Adminer)

### Services and Ports

- Backend (Spring Boot): `http://localhost:9090`
- Frontend (Vite dev): `http://localhost:5173`
- PostgreSQL (Docker): `localhost:5433`
- Adminer (DB UI): `http://localhost:8888`

### Quick start

From the repository root:

```bash
# 1) Start database
docker compose up -d

# 2) Start backend (Spring Boot)
directly run the BlogApplication by clicking the "run" button

# 3) Start frontend (Vite)
cd blog-platform-frontend
npm install
npm run dev
```

Open the apps:

- Frontend: `http://localhost:5173`

---
