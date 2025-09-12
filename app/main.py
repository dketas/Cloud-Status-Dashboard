from flask import Flask, jsonify, Response
import requests
from prometheus_client import generate_latest, Counter, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a counter metric to track how many times status checks have run
status_check_counter = Counter("status_check_total", "Total number of status checks performed")

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
    status_check_counter.inc()  # Increment on each status check call
    results = {}
    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            results[url] = "UP" if response.status_code == 200 else "DOWN"
        except requests.exceptions.RequestException:
            results[url] = "DOWN"
    return jsonify(results)

@app.route('/metrics')
def metrics():
    # Return Prometheus metrics with proper content type
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

