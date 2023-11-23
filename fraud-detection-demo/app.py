## prerequisite
# pip install Flask
# pip install flask_cors
# pip install flask_restful
# pip install flask_swagger_ui

import prediction
from flask import render_template, Response

from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
#from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def error_handler_404(error):
    return "Page not found", 404

# @app.errorhandler(Exception)
# def error_handler_exception(error):
#     return "An error occurred", 500  # Internal Server Error

#=== === === === === === === 

#print (request.base_url)
SWAGGER_URL  = '/swagger'
SWAGGER_JSON = 'swagger.json'
SWAGGER_JSON_URL = '/'+SWAGGER_JSON
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    SWAGGER_JSON_URL,
    config={'app_name': "Fraud Prediction API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route(SWAGGER_JSON_URL)
def swagger():
    with open(SWAGGER_JSON, 'r') as file:
        return jsonify(json.load(file))

#=== === === === === === ===

@app.route('/')
def root():
    #try:
    return render_template('root.html')
    #except Exception as e:
    #    return render_template('root.html')

#=== === === === === === ===

@app.route('/data/fields.json')
def get_data_fields():
    json_content = ""
    with open('data/fields.json', 'r') as file:
        json_content = file.read()
    response = Response(json_content, content_type='application/json')
    response.headers['Content-Disposition'] = 'filename=fields.json'
    return response

@app.route('/data/data.csv')
def get_data_file():
    data_content = ""
    with open('data/data.csv', 'r') as file:
        data_content = file.read()
    response = Response(data_content, content_type='text/txt')
    response.headers['Content-Disposition'] = 'filename=data.csv'
    return response

#=== === === === === === ===

@app.route('/api/prediction', methods=['POST'])
def api_prediction_post():
    return prediction.post(request)

#=== === === === === === ===