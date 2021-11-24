#import all library

import pandas as pd
import numpy as np
import tensorflow as tf
import json

import os

from sklearn.preprocessing import MinMaxScaler

#function to load model by using tensorflow
def load_model():
    model = tf.keras.models.load_model('best_model_crop_recommendation.h5')
    return model

#function to cast numeric label back to wordish prediction
def cast_label(prediction):
    with open('labelEncoder_dict.json', 'r') as file:
        labels = json.load(file)

    for key, value in labels.items():
        if str(prediction) == value:
            return key

#normalize the input range
def normalization(array_parameter):
    file_name = "Crop_recommendation.csv"
    df = pd.read_csv(file_name)

    minmaxScaler = MinMaxScaler()
    minmaxScaler.fit(df.iloc[:, 0:-1])

    array_scaled = minmaxScaler.transform(array_parameter)
    np_scaled = np.array(array_scaled)

    return np_scaled

#show input form
def show_input_form():
    n_val = -100
    p_val = -100
    k_val = -100
    temp_val = -100
    humid_val = -100
    ph_val = -100
    rain_val = -100

    while ( n_val < 0 ):
        n_val = float(input("Input N value\t\t: "))

    while ( p_val < 0 ):
        p_val = float(input("Input P value\t\t: "))

    while ( k_val < 0 ):
        k_val = float(input("Input K value\t\t: "))

    while ( temp_val < 0 ):
        temp_val = float(input("Input Temperature\t: "))
    
    while ( humid_val < 0 ):
        humid_val = float(input("Input Humidity\t\t: "))
    
    while ( ph_val < 0 ):
        ph_val = float(input("Input pH value\t\t: "))

    while ( rain_val < 0 ):
        rain_val = float(input("Input rainfall\t\t: "))

    input_list = [[n_val, p_val, k_val, temp_val, humid_val, ph_val, rain_val]]

    return input_list
    

#show main menu & menu list
def print_main_menu():
    choice = -1

    print("="*30)
    print("Agraris Model Menu")
    print("="*30, end="\n\n")

    print("1. Look for recommendation")
    print("2. Stop\n")

    while ( choice >= 3 or choice <= 0 ):
        choice = int(input("Input choice (1-2): "))

    if choice == 1:
        user_input = show_input_form()
        print(user_input)
        np_user_input_scaled = normalization(user_input)
        prediction = model.predict(np_user_input_scaled)
        result = cast_label(prediction)
        print("Best crop for you is: {}".format(result))
        choice = input("\nPress enter to continue...")

    elif choice == 2:
        quit()

    if os.name == 'posix':
      _ = os.system('clear')
    else:
      _ = os.system('cls')
      
    print_main_menu()

#LINK STARTTT
if __name__ == "__main__":
    model = load_model()
    print_main_menu()
        

# random samples picking
# test_pred = normalization([[108,22,46,26.17668721,86.72952049999998,6.121168559,53.33484977]])
# test_pred2 = normalization([[90,42,43,20.87974371,82.00274423,6.502985292000001,202.9355362]]) -> should predict "rice"
# test_pred3 = normalization([[24,140,205,12.087022,83.59398734,5.93202852,68.66813363]])

# prediction = model.predict(test_pred)
# prediction2 = model.predict(test_pred2)
# prediction3 = model.predict(test_pred3)

