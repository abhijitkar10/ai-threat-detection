from flask import Flask, request, jsonify
import mysql.connector
import time

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="threatdb"
    )

# Wait until DB is ready (proper way)
while True:
    try:
        db = get_db_connection()
        break
    except:
        print("Waiting for DB...")
        time.sleep(2)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    log TEXT,
    prediction VARCHAR(50)
)
""")
db.commit()


@app.route("/analyze", methods=["POST"])
def analyze():
    log = request.json["log"]
    prediction = "attack" if "failed" in log.lower() else "normal"

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO alerts (log, prediction) VALUES (%s, %s)",
        (log, prediction)
    )
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)