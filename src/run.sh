rm -rf app/data.db
touch app/data.db
export FLASK_ENV=development
python3 app/app.py
