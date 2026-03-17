from flask import Flask, request, session, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"   # IMPORTANT

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="vishal@1234",
        database="Flask_db"
    )

# Home route
@app.route("/")
def home():
    return '''
    <h2>Login Page</h2>
    <form action="/login1" method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
    '''

# Login route
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
        return "Invalid Username or Password"

# Dashboard
@app.route("/dashboard1")
def dashboard():
    if "user" in session:
        return "Welcome " + session["user"]
    else:
        return redirect(url_for("home"))

# Logout
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)