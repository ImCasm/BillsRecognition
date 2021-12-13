class PredictionRequest:
    def __init__(self, id_client, images, models):
        self.id_client = id_client
        self.images = images
        self.models = models
