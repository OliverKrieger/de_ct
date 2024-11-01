import requests

def get_data():
    response = requests.get("http://date.jsontest.com/")
    if response.ok:
        return response.json()
    return {"error": "Failed to fetch date data"}