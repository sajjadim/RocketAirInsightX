# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib


# Load the dataset
df = pd.read_csv('final4.csv')

# Separate the feature and target variables
X = df.drop(['Vehicle', 'Mixing_ratio_Al_if_Solid_main',
               'Fuel_Type_booster', 'Total_Propellant_Mass_kg_booster',
             'Mixing_ratio_Al_if_Solid_booster', 'Stratospheric_CO2_tons',
             'Stratospheric_H2O_tons', 'Stratospheric_Black_Carbon_tons',
             'Stratospheric_NOx_tons', 'Stratospheric_nClx_tons',
             'Stratospheric_Alumina_tons', 'pollution'], axis=1)
y = df['pollution']

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r_squared = model.score(X_test, y_test)

print("Root Mean Squared Error:", rmse)
print("R-Squared:", r_squared)

for index, row in df.iterrows():
    new_data = pd.DataFrame({'Fuel_Type_main': [row['Fuel_Type_main']],
                             'Total_Propellant_Mass_kg_main': [row['Total_Propellant_Mass_kg_main']],
                             'max_altitude_km': [row['max_altitude_km']],
                             'total_fuel_mass': [row['total_fuel_mass']]})
    new_pred = model.predict(new_data)
    print("Predicted pollution: ", new_pred, "Real Value: ", row['pollution'])

joblib.dump(model, 'gradient_boosting_regression_model.joblib')

