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

## Load some initial data (recommended)

```
python3 manage.py loaddata fixtures/warehouses.json
python3 manage.py loaddata fixtures/items.json
```

## To start the server

```bash
python3 manage.py runserver
```

## To create a admin user (Another shell)

```bash
python3 manage.py createsuperuser
```

## Now local setup is done

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) or [localhost:8000](localhost:8000)
