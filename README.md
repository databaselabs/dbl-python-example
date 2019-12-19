Database labs Python Example
============================

This repository contains example code for connecting to a 
[databaselabs.io](https://www.databaselabs.io/) database.

This example uses the [psycopg2](http://initd.org/psycopg/) library.

These examples try to use [12 factor app guidelines](https://12factor.net/)

Setup
-----

[comment]: # (TODO add git clone instructions)

### using pipenv

It is recommended to use the [pipenv packaging tool](https://realpython.com/pipenv-guide/).
A `requirements.txt` file will also be provided if you would prefer to use the `virtualenv` workflow.

Run the following command to create a virtual environment and install the necessary dependencies.

```
pipenv install
```

Now activate the virtual environment.

```
pipenv shell
```

### .env file

The .env file is where you store your local secrets. It is important to make sure this file never
gets committed to git.

Use the .env.example file as a starting point.

```
cp .env.example .env
```

[comment]: # (TODO sections for editing the .env file)

```
python --version
```

## Running the code

```
python example_01.py
```
