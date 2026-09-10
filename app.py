import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Versioning info (all injected at build time via env vars) ---
APPLICATION_VERSION = os.environ.get("APPLICATION_VERSION", "0.0.0-local")
MODEL_VERSION = os.environ.get("MODEL_VERSION", "model-1")
GIT_COMMIT = os.environ.get("GIT_COMMIT", "unknown")


@app.route("/")
def home():
    return jsonify({
        "service": "mlops-cd-demo",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "application_version": APPLICATION_VERSION,
        "model_version": MODEL_VERSION,
        "git_commit": GIT_COMMIT,
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    value = float(data["value"])
    # Dummy ML prediction for teaching purposes
    prediction = value * 2
    return jsonify({
        "input": value,
        "prediction": prediction,
        "application_version": APPLICATION_VERSION,
        "model_version": MODEL_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#for the merge