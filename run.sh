rm -rf database.db
touch database.db
export FLASK_ENV=development
#from app import app 
python3 main.py 
#app.run(host='0.0.0.0', port=5000, debug=True)