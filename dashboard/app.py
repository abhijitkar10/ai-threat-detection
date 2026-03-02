from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="threatdb"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM alerts")
        data = cursor.fetchall()
        db.close()

        return f"<h1>DEBUG OUTPUT</h1><pre>{data}</pre>"

    except Exception as e:
        return f"<h1>ERROR</h1><pre>{str(e)}</pre>"

app.run(host="0.0.0.0", port=5000)