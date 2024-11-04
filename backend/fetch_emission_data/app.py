from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import zipfile
import os
import pandas as pd
from urllib.parse import urlparse
from io import BytesIO
import logging
import json

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route("/fetch_emission_data", methods=["GET"])
def fetch_emission_data():
    logging.info('Fetching data from ZIP')
    url = request.args.get("url")
    payload = request.args.get("payload")
    if payload:
        payload = json.loads(payload)
    else:
        return jsonify({"error": "playload parameter is required"}), 400
    
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
            file_list = z.namelist()
            csv_filename = f"{zip_name}.csv"
            if csv_filename in file_list:
                logging.info('CSV to JSON')
                with z.open(csv_filename) as csv_file:
                    df = pd.read_csv(csv_file, dtype=str, encoding='latin1') # make dataframe
                    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
                    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
                    df = df.fillna("")
                    data = filterData(df.to_dict(orient='records'), payload)  # Convert to JSON
                    return jsonify(data)
            else:
                logging.error("No CSV file found in the ZIP archive.")
                return jsonify({"error": str(e)}), 500

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {str(e)}")
        return jsonify({"error": str(e)}), 500 # if error here, return 500 error

def filterData(records_data:dict, payload:any) -> dict:
    print("Filtering Data...")
    start_year = payload.get('startYear')
    end_year = payload.get('endYear')
    selected_item = payload.get('item')
    selected_element = payload.get("element")
    selected_countries = payload.get('countries')
    
    filteredData:dict = {}
    for entry in records_data:
        if entry["Element"] == selected_element and entry["Year"] >= start_year and entry["Year"] <= end_year and entry["Item"] == selected_item and entry["Area"] in selected_countries:
            if entry["Area"] not in filteredData:
                filteredData[entry["Area"]] = {
                    "Area Code": entry["Area Code"],
                    "Years": [],
                    "Values":[]
                }
            filteredData[entry["Area"]]["Years"].append(entry["Year"])
            filteredData[entry["Area"]]["Values"].append(entry["Value"])

    return filteredData