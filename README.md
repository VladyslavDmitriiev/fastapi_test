# README

## backend
- fastapi

## db
- PostgreSQL https://postgresapp.com/downloads.html
- pgAdmin https://www.pgadmin.org/download/

Create revision
```bash
alembic revision --autogenerate -m "commit message"
```

Execute migration
```bash
alembic upgrade revision_id
```