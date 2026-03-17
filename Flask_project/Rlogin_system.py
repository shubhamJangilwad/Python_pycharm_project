from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# Dummy user (like database)
valid_username = "admin"
valid_password = "1234"

# Show login page
@app.route("/")
def home():
    return render_template("login1.html")

# Handle login
@app.route("/login1", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Check credentials
    if username == valid_username and password == valid_password:
        session["user"] = username
        return redirect(url_for("dashboard"))
    else:
        return render_template("login1.html", error="Invalid username or password")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        return redirect(url_for("home"))

# Logout
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)