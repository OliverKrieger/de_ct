from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import zipfile
import os
import pandas as pd
from urllib.parse import urlparse
from io import BytesIO
import logging

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route("/fetch_emission_data", methods=["GET"])
def fetch_emission_data():
    logging.info('Fetching data from ZIP')
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "URL parameter is required"}), 400 # if no url variable given, return 400

    try:
        response = requests.get(url) # make request
        response.raise_for_status()

        logging.info('Extract ZIP to CSV')
        parsed_url = urlparse(url)
        zip_filename = os.path.basename(parsed_url.path)
        zip_name = os.path.splitext(zip_filename)[0] # Remove the ".zip" extension

        with zipfile.ZipFile(BytesIO(response.content)) as z:
            # List of files in the ZIP
            file_list = z.namelist()
            csv_filename = f"{zip_name}.csv"
            if csv_filename in file_list:
                logging.info('CSV to JSON')
                with z.open(csv_filename) as csv_file:
                    df = pd.read_csv(csv_file, encoding='latin1') # make dataframe
                    # data = df.to_json(orient='records')  # Convert to JSON
                    data = filterData(df.to_dict(orient='records'))  # Convert to JSON
                    return jsonify(data)
            else:
                logging.error("No CSV file found in the ZIP archive.")
                return jsonify({"error": str(e)}), 500

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {str(e)}")
        return jsonify({"error": str(e)}), 500 # if error here, return 500 error

def filterData(records_data:dict) -> dict:
    filteredData:dict = {}
    for entry in records_data:
        if entry["Element"] == "Crops total (Emissions N2O)" and entry["Year"] >= 1970 and entry["Year"] <= 2020 and entry["Item"] == "Barley" and (entry["Area"] == "United Kingdom of Great Britain and Northern Ireland" or entry["Area"] == "Portugal"):
            if entry["Area"] not in filteredData:
                filteredData[entry["Area"]] = {
                    "Area Code": entry["Area Code"],
                    "Values": []
                }
            filteredData[entry["Area"]]["Values"].append((entry["Year"], entry["Value"]))

    return filteredData