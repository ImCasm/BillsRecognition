from flask import Flask, jsonify, request

from app.classes.Prediction import Prediction
from app.classes.PredictionRequest import PredictionRequest
from app.services.PredictionService import PredictionService


def create_app():
    return Flask(__name__)


app = create_app()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        body = request.get_json(force=True)
        pred_request = PredictionRequest(body['id_client'], body['images'], body['models'])
        response = PredictionService().predict(pred_request)
        print(response)
        return jsonify(response)
    except:
        resp = {
            'state': "error",
            'message': "Error al realizar las predicciones"
        }
        return jsonify(resp), 400, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)


