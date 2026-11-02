
import logging
import pandas as pd
import pickle as pkl
from datetime import datetime

logger = logging.getLogger("uvicorn.error")
class FastAPIHandler:

    def __init__(self):
        logger.warning('Loading model...')
        try:
            self.model = pkl.load(open('service/models/model.pkl', 'rb'))
            logger.info('Model is loaded')
        except Exception as e:
            logger.error('Error loading model')

    def predict(self, item_id, item_features:dict):
        item_df = pd.DataFrame(data=item_features, index=[0])
        try:
            prediction = self.model.predict(item_df)
            return prediction[0]

        except Exception as e:
            logger.error(f"Ошибка внутри sklearn.predict: {str(e)}")
            raise e