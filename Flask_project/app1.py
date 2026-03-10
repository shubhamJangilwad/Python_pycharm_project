from flask import Flask

app = Flask(__name__)

@app.route("/cube/<int:num>")
def cube(num):
    result = num * num * num
    return "cube is : "+ str(result)

if __name__ == "__main__":
    app.run(debug=True)