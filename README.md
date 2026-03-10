# telegram-bot-codex

Production-oriented Telegram RPG bot scaffold.

## Stack
- Python 3.12
- aiogram 3.x
- SQLAlchemy 2.0 async
- PostgreSQL
- Alembic
- Redis

## Project structure
- `app/handlers`: Telegram handlers (thin transport layer)
- `app/services`: business logic
- `app/repositories`: database access
- `app/models`: ORM models
- `app/database`: SQLAlchemy base/session
- `app/middlewares`: cross-cutting concerns
- `app/states`: FSM states
- `app/config`: settings and logging
- `alembic/`: migrations

## Quick start
1. Copy `.env.example` to `.env` and set values.
2. Run: `docker compose up --build`

Container startup runs:
1. `alembic upgrade head`
2. `python -m app.main`

## Dev checks
- `pytest -q`
