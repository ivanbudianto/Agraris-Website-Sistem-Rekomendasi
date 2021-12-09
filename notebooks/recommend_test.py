# Import all library
import numpy as np
import tensorflow as tf
import json
import os

# Function to load model by using tensorflow
def load_model():
  model = tf.keras.models.load_model('models/best_model_crop_recommendation.h5')
  return model

# Function to cast numeric label back to wordish prediction
def cast_label(prediction):
  result = np.argmax(prediction)

  with open('recommend_dic.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == value:
      return key

# Normalize the input range
def normalization(array_parameter):
  # Value is retrieved from the df.describe()
  min_val = [0, 5 ,5, 8.825675, 14.258040, 3.504752, 20.211267]
  max_val = [140, 145, 205, 43.675493, 99.981876, 9.935091, 298.560117]

  for i in range(len(array_parameter[0])):
    array_parameter[0][i] = (array_parameter[0][i] - min_val[i]) / (max_val[i] - min_val[i])

  np_scaled = np.array(array_parameter)
  return np_scaled

# Show input form
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

# Show main menu & menu list
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

# LINK STARTTT
if __name__ == "__main__":
  model = load_model()
  print_main_menu()

# TEST DATA -> should predict "rice"
# [[90,42,43,20.87974371,82.00274423,6.502985292000001,202.9355362]]

