import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:1011@localhost:5432/contacts"  # Замініть на ваші налаштування
)
