from flask import Flask , session

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/set")
def set_data():
    session["name"] = "Rahul"
    return "Session stored"

@app.route("/get")
def get_data():
    return session["name"]

if __name__ == "__main__":
    app.run(debug=True)