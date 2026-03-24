from flask import Flask , render_template , redirect , url_for , request,session

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods = ["POST"])
def login():
    username = request.form["username"]
    session["user"] = username
    password = request.form["password"]
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return "welcome " + session["user"]
    else:
        return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("user")
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)