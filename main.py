from flask import Flask, jsonify, request
from app.classes.PredictionRequest import PredictionRequest
from app.services.PredictionService import PredictionService


def create_app():
    return Flask(__name__)


app = create_app()

@app.route('/predict', methods=['POST'])
def predict():
    body = request.get_json(force=True)
    pred_request = PredictionRequest(body['id_client'], body['images'], body['models'])
    response = PredictionService().predict(pred_request)
    print(response)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
