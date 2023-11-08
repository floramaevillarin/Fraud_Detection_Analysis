## prerequisite
# pip install Flask
# pip install flask_restful
# pip install flask_swagger_ui

import page_form01_controller
import api_prediction

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def error_handler_404(error):
    return "Page not found", 404

@app.errorhandler(Exception)
def error_handler_exception(error):
    return "An error occurred", 500  # Internal Server Error

### ### ### ### ### ### ### ### ### 

#print (request.base_url)
SWAGGER_URL = '/swagger'
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

### ### ### ### ### ### ### ### ### 

@app.route('/', methods=['GET', 'POST'])
def root():
   return page_form01_controller.process(request)

### ### ### ### ### ### ### ### ### 

@app.route('/api/prediction', methods=['GET'])
def api_prediction_get():
    return api_prediction.get(request)

### ### ### ### ### ### ### ### ### 