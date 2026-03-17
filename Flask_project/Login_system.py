from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# Show login page
@app.route("/")
def home():
    return render_template("login.html")

# Handle login
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    session["user"] = username
    return redirect(url_for("dashboard"))

# Dashboard (protected)
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