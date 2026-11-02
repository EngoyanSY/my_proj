import logging
import os

import pandas as pd
import pickle as pkl

logger = logging.getLogger("uvicorn.error")
class FastAPIHandler:

    def __init__(self):
        logger.warning('Loading model...')

        if os.path.exists('/models/model.pkl'):
            model_path = '/models/model.pkl'
        else:
            model_path = os.path.join(os.path.dirname(__file__), '../models/model.pkl')

        try:
            self.model = pkl.load(open(model_path, 'rb'))
            logger.info(f'Model is successfully loaded from {model_path}')
        except Exception as e:
            logger.error(f'Error loading model: {str(e)}')

    def predict(self, item_id, item_features:dict):
        item_df = pd.DataFrame(data=item_features, index=[0])
        try:
            prediction = self.model.predict(item_df)
            return prediction[0]

        except Exception as e:
            logger.error(f"Ошибка внутри sklearn.predict: {str(e)}")
            raise e