# Run the project

```bash
docker compose up --build -d
```

## Generate alembic migration

```bash
docker exec ms-due-diligence-api alembic revision --autogenerate -m "your message"
```

Apply it:

```bash
docker exec ms-due-diligence-api alembic upgrade head
```
