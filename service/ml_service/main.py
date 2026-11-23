from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary

from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted gpa',
    buckets=(2.0, 2.5, 3.0, 3.5, 4.0)
)

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(item_id: int, item_features: dict):
    prediction = app.handler.predict(item_id, item_features)

    prediction_metric.observe(prediction)

    return ({
             'POST_GPA': prediction,
             'flat_id': item_id,
            })