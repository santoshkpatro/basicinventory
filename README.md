Simple and Basic Inventory Management Software

### Tech Stack

- Django
- Bootstrap

### Requirements

- python3
- sqlite (Installation not required)

## Installation (Linux/MacOS)

Step 1(Create and activate virtual env)

```bash
# Creating virtual env
python3 -m venv venv

# activating
source venv/bin/activate
```

## Migrate the DB changes

```bash
python3 manage.py migrate
```

## To start the server

```bash
python3 manage.py runserver
```

## To create a admin user (Another shell)

```bash
python3 manage.py createsuperuser
```
