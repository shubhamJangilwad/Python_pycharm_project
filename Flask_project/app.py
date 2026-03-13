from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    city = request.form["city"]
    return redirect(url_for("result",city=city))

@app.route("/result/<city>")
def result(city):
    return "you entered: "+ city


if __name__ == "__main__":
    app.run(debug=True)
