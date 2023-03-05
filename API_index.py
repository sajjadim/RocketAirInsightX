from Predicting  import predict
from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import requests
from ChatGpt import ChatEnchancementSuggestion,ChatWritingOverview
app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict',methods=['GET','POST'])
def onPredict():
    jsonArguments = request.get_json()
    predicted_data = predict(jsonArguments['fuel_type'],jsonArguments['total_propellant_mass'] ,jsonArguments['max_altitude'] ,jsonArguments['total_fuel_mass'] )
    chat_enhancement_result = ChatEnchancementSuggestion(jsonArguments['chat_suggestion_template'], jsonArguments['chat_suggestion_data'],int(predicted_data))
    print(predicted_data)
    response = jsonify({'pollution': int(predicted_data),'chat_result': chat_enhancement_result})
    response.headers.add('Access-Control-Allow-Origin', '*');
    
    return response


    
@app.route('/')
def home():
    return "Welcome to Rocket Emission Prediction App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)