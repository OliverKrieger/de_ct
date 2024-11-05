from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import logging
import os

CUSTOM_API_KEY = os.getenv("VITE_FUNCTION_HOST_KEY")

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route("/fetch_data", methods=["GET"])
def fetch_data():
    request_key = request.args.get("code")
    if request_key != CUSTOM_API_KEY:
        return jsonify({"error": "Invalid API Key"}), 403

    logging.info('Fetching data from URL.')
    url = request.args.get("url") # get url from path
    
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400 # if no url variable given, return 400

    try:
        response = requests.get(url) # make request
        response.raise_for_status()
        data = response.json() # convert to json
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {str(e)}")
        return jsonify({"error": str(e)}), 500 # if error here, return 500 error

    return jsonify(data) # otherwise return data from request