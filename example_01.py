#!/usr/bin/env python3
import psycopg2

from config import Config


def main():
    # creates a connection to the existing database
    conn = psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        sslmode=Config.DB_SSLMODE)

    #
    cur = conn.cursor()

    #
    cur.execute("CREATE TABLE test (id SERIAL PRIMARY KEY, name VARCHAR, email VARCHAR);")

    #
    cur.execute("INSERT INTO test (name, email) VALUES (%s, %s)", ("Tony", "tony@example.com"))

    #
    cur.execute("SELECT * FROM test;")

    #
    first = cur.fetchone()

    #
    print(first)

    #
    cur.execute("DROP TABLE test;")

    #
    conn.commit()

    #
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
