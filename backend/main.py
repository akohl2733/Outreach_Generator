from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def main_page():
    return "<p>this is the home page</p>"

@app.route("/test")
def tester():
    return jsonify({"status": "this is working properly"})

if __name__ == "__main__":
    app.run(debug=True, port=8081)

