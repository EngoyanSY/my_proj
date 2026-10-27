
import logging
import pandas as pd
import pickle as pkl
import psycopg2
from datetime import datetime

logger = logging.getLogger("uvicorn.error")
class FastAPIHandler():

    def __init__(self):
        pass
        # logger.warning('Loading model...')
        # try:
        #     self.model = pkl.load(open('../models/model.pkl', 'rb'))
        #     logger.info('Model is loaded')
        # except Exception as e:
        #     logger.error('Error loading model')

    # def predict(self, flat_id, item_features:dict):
    #     item_df = pd.DataFrame(data=item_features, index=[0])
    #     prediction = self.model.predict(item_df)

    #     db_cred = {"dbname": "my_db_name",
    #                "user": 'admin',
    #                "password": 'admin',
    #                "host": "database"}
        
    #     db_conn = psycopg2.connect(**db_cred)
    #     cur = db_conn.cursor()

    #     now = datetime.now()
    #     cur.execute(f"INSERT INTO public.features \
    #                 (flat_id, ts, geo_lon, geo_lat, area) \
    #                 VALUES ({flat_id}, '{now}', {item_features['geo_lon']}, {item_features['geo_lat']}, {item_features['area']});")
    #     cur.execute(f"INSERT INTO public.predictions \
    #                 (flat_id, ts, price) VALUES ({flat_id}, '{now}', {prediction[0]});")

    #     db_conn.commit()

    #     return (prediction[0])