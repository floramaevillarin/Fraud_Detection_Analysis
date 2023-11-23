import sklearn
import joblib
import pandas as pd

from flask import Flask, request, jsonify

#=== === === === === ===

def post(request):
    try:
        # Get the JSON data from the request
        data_json = request.json

        # If come all params ...
        validate(data_json)

        homo_json = homologate(data_json)
        
        # Get the prediction 
        result = prediction(homo_json)
        
        save_data(data_json, result)

        response = {'result': result}
        return jsonify(response)

    except Exception as ex:
        # throwing the error in result
        error_msg = 'ERROR: '+ex.args[0]
        save_data(data_json, error_msg)

        response  = {'result': error_msg}
        return jsonify(response), 400  # 400 Bad Request

#=== === === === === ===

def validate(data_json):
    # If come all params ...
    if not ('param01' in data_json and 'param02' in data_json and 'param03' in data_json and 'param04' in data_json and 'param05' in data_json):
        # throwing the error in result
        raise Exception("Parameters required")

#=== === === === === ===

def homologate(data_json):
    param01 = int(data_json['param01'])
    param02 = int(data_json['param02'])
    param03 = int(data_json['param03'])
    param04 = int(data_json['param04'])
    param05 = int(data_json['param05'])
    
    homo_json = {
        "a": [param01],  # 1
        "b": [param02],  # 11
        "c": [param03],  # 21
        "d": [param04],  # 31
        "e": [param05]   # 41
    }
    return homo_json

#=== === === === === ===

def prediction(data_json):
    sklearn_version = sklearn.__version__
    filename = f'models/model_joblib_{sklearn_version}.pkl'

    model_loaded = joblib.load(filename)
    y_pred = model_loaded.predict(pd.DataFrame(data_json))
    return str(y_pred[0])

#=== === === === === ===

def save_data(data_json, result):
    data_file_path = "data/data.csv"
    with open(data_file_path, 'a') as file:
        new_line = json_csv_line(data_json) + ", " + result
        file.write('\n'+new_line)

def json_csv_line(data_json):
    return ', '.join([f'{value}' for key, value in data_json.items()])

#=== === === === === ===