
from flask import Flask, jsonify
import requests

app = Flask(__name__)

URLS = [
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts",
    "https://www.google.com",
    "https://example.com"
]

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Cloud Status Dashboard", 200

@app.route('/status', methods=['GET'])
def get_status():
    results = {}
    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            results[url] = "UP" if response.status_code == 200 else "DOWN"
        except:
            results[url] = "DOWN"
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

