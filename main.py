from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello world"


@app.route("/test/<search_query>")
def search(search_query):
    return search_query


@app.route("/<int:value>")
def int_type(value):
    print(value)
    return "Integer Type Correct"


@app.route("/<float:value>")
def float_type(value):
    print(value)
    return "Float Type Correct"


@app.route("/<path:value>")
def path_type(value):
    print(value)
    return "Path Type Correct"


if __name__ == "__main__":
    app.run()
