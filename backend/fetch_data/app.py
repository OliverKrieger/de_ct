from flask import Flask, jsonify, request
import requests
import logging

app = Flask(__name__)

@app.route("/fetch_data", methods=["GET"])
def fetch_data():
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