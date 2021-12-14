from app.classes import ImageConverter
from app.classes.Model import Model
from app.classes.Prediction import Prediction
import cv2


class PredictionService:
    def __init__(self):
        self.models = [
            Model(1, 'app/models/model1.h5'),
            Model(2, 'app/models/model2.h5'),
            Model(3, 'app/models/model3.h5')
        ]
        self.classes = [1000, 2000, 5000, 10000, 20000]

    def predict(self, request):
        results = []
        for model in self.models:
            model_results = []
            if model.model_id in request.models:
                for image in request.images:
                    result = self.predict_single(model.path, ImageConverter.base64_to_img(image['content'], image['id']))
                    model_results.append({
                        'class': result,
                        'id_image': image['id']
                    })
                results.append({
                    'model_id': model.model_id,
                    'results': model_results
                })

        return {
            'state': 'success',
            'message': 'Las predicciones de realizaron correctamente',
            'results': results
        }

    def predict_single(self, model, image_path):
        model = Prediction(model, 256, 256)
        image = cv2.imread(image_path)
        result_class = model.predecir(image)
        return self.classes[result_class]
