rm -rf app/data.db
touch app/data.db
export FLASK_ENV=development
#from app import app 
python3 app/app.py
#app.run(host='0.0.0.0', port=5000, debug=True)