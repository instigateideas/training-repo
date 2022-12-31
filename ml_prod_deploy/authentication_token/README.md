# Database - SQLite Setup

# Feature Implemented
The Feature implemented in this code:

1. ML Prediction - REST API (flask)
2. Logging 
3. IP Restriction
4. Token Based Authentication (registration of new user, login, get_token)

## Install the SQLite DB (Prod - Linux)
```bash
sudo apt-get install sqlite3
```

## Create the Database
```bash
sqlite3 register.db
```

## Check whether the DB is created - Inside SQLite CLI
.databases

Before generating the users make sure the configuration of app part is done and models are created.

## Generate Users and Authors Tables - open python
On the terminal type the below code inside the virtual environment
```python
>>> from app import app
>>> from app import db
>>> db.create_all()
>>> exit()
```


