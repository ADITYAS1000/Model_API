from flask import Flask, request, jsonify
from model import *

flask_app = Flask(__name__)
flask_app.config["DEBUG"] = True

@flask_app.route("/", methods=["GET"])
def health():
    if request.method == "GET":
        return "Working Fine"

@flask_app.route("/predict", methods=['POST'])
def inference():
    if request.method == 'POST':
        json_data = request.get_json()

        result = predict(input_data=json_data)

        return jsonify(result)

if __name__ == "__main__":
	
    flask_app.run()