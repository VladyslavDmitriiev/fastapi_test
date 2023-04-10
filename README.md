# README

## backend
- fastapi

## db
- PostgreSQL https://postgresapp.com/downloads.html
- pgAdmin https://www.pgadmin.org/download/

## Project structure
```md
project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   └── products.py
│   │   │   └── schemas/
│   │   │       ├── __init__.py
│   │   │       ├── users.py
│   │   │       └── products.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── __init__.py
│   │   └── db/
│   │       ├── base.py
│   │       ├── __init__.py
│   │       ├── session.py
│   │       └── models/
│   │           ├── __init__.py
│   │           ├── users.py
│   │           └── products.py
│   ├── alembic.ini
│   ├── alembic/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── docker-compose.yml
└── frontend/
    ├── public/
    │   ├── index.html
    │   └── favicon.ico
    ├── src/
    │   ├── components/
    │   │   ├── Header.js
    │   │   ├── Footer.js
    │   │   └── ...
    │   ├── pages/
    │   │   ├── HomePage.js
    │   │   ├── LoginPage.js
    │   │   ├── ProductPage.js
    │   │   └── ...
    │   ├── App.js
    │   ├── index.js
    │   ├── utils.js
    │   └── ...
    ├── Dockerfile
    ├── package.json
    ├── yarn.lock
    └── Dockerfile
```

Here's a brief overview of what each directory/file does:

backend: This directory contains your FastAPI backend code, as well as an alembic directory with the migration scripts, a Dockerfile and a docker-compose.yml file to help with containerization and deployment.

frontend: This directory contains your React frontend code, as well as the dependencies needed to run it (contained within the package.json file). Again, there's also a Dockerfile to help with containerization and deployment.

backend/app: This directory contains the main FastAPI application, including the API routes, and schemas.

backend/core: This directory contains code related to configuration, authentication/authorization, and security.

backend/db: This directory contains code and models for your application's database. It employs SQLAlchemy as an ORM to interact with PostgreSQL.