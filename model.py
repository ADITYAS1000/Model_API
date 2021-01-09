import json

from keras.models import load_model
from conv_helper import *

def predict(input_data) -> list:
    """Make a prediction using the saved model"""
    #print(input_data)
    input_data = json.loads(input_data) # Comment for POSTMAN
    type, data = input_data['type'], input_data['data']
    
    if type == 'conv':
        model = load_model(r"chatbot_model.h5")
        result = predict_class(data, model)
        #print(data, result)

    return result
