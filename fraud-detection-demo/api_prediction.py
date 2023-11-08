import lib_business

from flask import Flask, request, jsonify

def get(request):
    try:
        # Get the JSON data from the request
        data = request.json

        # If come all params ...
        if not ('param01' in data and 'param02' in data and 'param03' in data and 'param04' in data and 'param05' in data):
            # throwing the error in result
            response = {'result': 'ERROR: Parameters required'}
            return jsonify(response), 400  # 400 Bad Request

        param01 = int(data['param01'])
        param02 = int(data['param02'])
        param03 = int(data['param03'])
        param04 = int(data['param04'])
        param05 = int(data['param05'])
        
        data_json = {
            "a": [param01],  # 1
            "b": [param02],  # 11
            "c": [param03],  # 21
            "d": [param04],  # 31
            "e": [param05]   # 41
        }
        
        # Get the prediction 
        result = lib_business.prediction(data_json)
        
        response = {'result': str(result)}
        return jsonify(response)

    except Exception as e:
        # throwing the error in result
        response = {'result': 'ERROR: '+e.args[0]}
        return jsonify(response), 400  # 400 Bad Request
    