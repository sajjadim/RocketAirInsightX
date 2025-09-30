# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib


def predict(fuel_Type, total_Propellant_Mass, max_altitude, total_fuel_mass):
    
    model = joblib.load('gradient_boosting_regression_model.joblib')
    new_data = pd.DataFrame({'Fuel_Type_main': [fuel_Type],
                             'Total_Propellant_Mass_kg_main': [total_Propellant_Mass],
                             'max_altitude_km': [max_altitude],
                             'total_fuel_mass': [total_fuel_mass]})
    output= model.predict(new_data);
    output_value =  output[0]
    output_value_int =  int(output[0])
    print(f'Prediction Result: {output_value_int} Kg pollution')
    return output_value_int

