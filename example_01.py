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

    # Create a cursor to work with the database
    cur = conn.cursor()

    # Creates a simple Table
    cur.execute("CREATE TABLE test (id SERIAL PRIMARY KEY, name VARCHAR, email VARCHAR);")

    # Inserts a single row into the table
    cur.execute("INSERT INTO test (name, email) VALUES (%s, %s);", ("Tony", "tony@example.com"))

    # Executes a select on the current table
    cur.execute("SELECT * FROM test;")

    # Gets the first Item returned from the select
    first = cur.fetchone()

    # Displays the result
    print(first)

    # Deletes the table that was created
    cur.execute("DROP TABLE test;")

    # Finishes the Transaction
    conn.commit()

    # Closes the Cursor and database connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
