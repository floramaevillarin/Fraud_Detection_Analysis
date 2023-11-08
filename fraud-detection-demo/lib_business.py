import sklearn
import joblib
import pandas as pd

def prediction(data_json):
    sklearn_version = sklearn.__version__
    filename = 'model_joblib_{sklearn_version}.pkl'.format(sklearn_version=sklearn_version)

    model_loaded = joblib.load(filename)
    y_pred = model_loaded.predict(pd.DataFrame(data_json))
    return int(y_pred[0])