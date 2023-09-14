rm db.sqlite3
rm -rf ./fitfolioapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations fitfolioapi
python3 manage.py migrate fitfolioapi
python3 manage.py loaddata users
python3 manage.py loaddata exercisetypes
python3 manage.py loaddata exercises
python3 manage.py loaddata workouts