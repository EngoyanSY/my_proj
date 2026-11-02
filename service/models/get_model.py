import os

import mlflow
import pickle as pkl

# Настройка URI (как в вашем коде)
TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000
mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}")

MODEL_NAME = "best_model_gpa"
MODEL_VERSION = "1"

# Загружаем модель напрямую из Реестра моделей
loaded_model = mlflow.sklearn.load_model(f"models:/{MODEL_NAME}/{MODEL_VERSION}")

save_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

with open(save_path, 'wb+') as f:
    pkl.dump(loaded_model, f)