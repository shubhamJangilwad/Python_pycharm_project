from flask import Flask

app = Flask(__name__)

@app.route("/square/<int:num>")
def square(num):
    result = num * num
    return "square is  : "+ str(result)

if __name__ == "__main__":
    app.run(debug=True)