from flask import Flask , render_template , redirect , url_for , request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form1.html")

@app.route("/submit" ,methods=["POST"])
def submit():
    name = request.form["name"]
    return redirect(url_for("result1",name = name))

@app.route("/result1/<name>")
def result1(name):
    return "you entered: " + name

if __name__ == "__main__":
    app.run(debug=True)