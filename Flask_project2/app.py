from flask import Flask, request, session, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="vishal@1234",
        database="Flask_db"
    )

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login1", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        session["user"] = username
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html", error="Invalid credentials")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True,port=8000)