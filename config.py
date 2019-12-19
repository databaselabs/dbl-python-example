import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # defines the connection parameters for our database
    DB_NAME = os.getenv("DB_NAME", "app")
    DB_USER = os.getenv("DB_USER", "app")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", 5432)

    # @link https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNECT-SSLMODE
    DB_SSLMODE = os.getenv("DB_SSLMODE", "require")
