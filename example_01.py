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

    # Inserts another row into the table
    cur.execute("INSERT INTO test (name, email) VALUES (%s, %s);", ("Sue", "sue@example.com"))

    # Executes a select on the current table
    cur.execute("SELECT * FROM test;")

    # Gets the first row returned from the select
    first = cur.fetchone()

    # Gets the next row
    second = cur.fetchone()

    # If there are no more rows `None` will be returned
    third = cur.fetchone()

    # Displays the result
    print(first)  # `(1, 'Tony', 'tony@example.com')`
    print(second)  # `(2, 'Sue', 'sue@example.com')`
    print(third)  # `None`

    # Inserts multiple rows into the table with a single query
    cur.execute("INSERT INTO test (name, email) VALUES (%s, %s), (%s, %s), (%s, %s);", (
        "Erin", "erin@example.com",
        "Doug", "doug@example.com",
        "Jan", "jan@example.com",
    ))

    # Executes a select with an order by, limit, and offset
    cur.execute("SELECT * FROM test ORDER BY id LIMIT 2 OFFSET 2;")

    # Fetch all the results stored in the cursor as a list
    results = cur.fetchall()

    print(results)  # `[(3, 'Erin', 'erin@example.com'), (4, 'Doug', 'doug@example.com')]`

    # Deletes the table that was created
    cur.execute("DROP TABLE test;")

    # Finishes the Transaction (A new transaction will automatically be created)
    conn.commit()

    # you can also rollback the transaction if something went wrong
    cur.execute("CREATE TABLE mistake (id SERIAL PRIMARY KEY, blunder VARCHAR, fault VARCHAR);")
    conn.rollback()

    # Closes the Cursor and database connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
