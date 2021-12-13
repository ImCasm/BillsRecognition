from app.models import ImageConverter
from app.models.Model import Model

class Prediction:
    def __init__(self):
        self.models =  [
            Model(1, 'models/model1'),
            Model(2, 'models/model2'),
            Model(3, 'models/model3')
        ]

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

    def predict_single(self, model, image):
        print(image)
        return 0