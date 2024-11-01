from flask import Flask, jsonify
from flask_cors import CORS

from data_request import get_data

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})

@app.route("/get-data", methods=["GET"])
def date():
    data = get_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=7071)