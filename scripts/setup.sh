#/bin/bash

# FUNCTIONS
echo_red() {
    echo -e "\x1b[1;31m$1\e[0m"
}

# VIRTUAL ENVIRONMENT
echo_red "Setting up disposable virtual environment"
python3 -m pip install --user virtualenv 2>&1 1>/dev/null
python3 -m venv venv 2>&1 1>/dev/null
source ./venv/bin/activate 2>&1 1>/dev/null

# DEPENDENCIES
echo_red "Installing dependencies"
pip3 install -r ./requirements.txt 2>&1 1>/dev/null

# POSTGRESQL
echo_red "Setting up Postgres database"
dropdb shop_inventory 2>&1 1>/dev/null
createdb shop_inventory 2>&1 1>/dev/null
echo "DATABASE_NAME='shop_inventory'" > ./.env

# TABLES AND SEEDS
echo_red "Importing and seeding tables into database"
psql -d shop_inventory -f ./src/db/shop_inventory.sql
python3 src/seeds.py 2>&1 1>/dev/null

# RUNNING APP
echo_red "Starting up Flask application"
open "http://127.0.0.1:5000/"
python3 -m flask run

exit 0