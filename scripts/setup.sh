# don't run this setup script. still working on it.
# ROOT="$(awk 'END{ var=FILENAME; split (var,a,/\//); print a[5]}' $PWD)"

dropdb shop_inventory
createdb shop_inventory
echo "DATABASE_NAME='shop_inventory'" > ./.env

# install from requirements.txt
python3 -m pip install --user virtualenv
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r ./requirements.txt

# createdb
# import tables to db
psql -d shop_inventory -f ./src/db/shop_inventory.sql
# populate db

python3 src/seeds.py
# flask run/ python3 -m flask run (whichever works)
open "http://127.0.0.1:5000/"
python3 -m flask run

deactivate
rm -rf ./venv
rm ./.env
exit 0

# check if runs
# open browser with whatever local url running

