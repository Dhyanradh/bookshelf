from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)


DB_HOST = "bookshelf-db.cl4ua8woc9si.eu-north-1.rds.amazonaws.com"
DB_NAME = "bookshelf"
DB_USER = "vangogh"
DB_PASS = "nickalm123"  

def check_credentials(username, password):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, password)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user is not None
    except Exception as e:
        print("Database error:", e)
        return False

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if check_credentials(username, password):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
