#/bin/bash

# FUNCTIONS
echo_red() {
    echo -e "\x1b[1;31m$1\e[0m"
}

# CLEAN UP
echo_red "Cleaning up virtual environment..."
deactivate
dropdb shop_inventory
rm -rf ./venv
rm ./.env

exit 0