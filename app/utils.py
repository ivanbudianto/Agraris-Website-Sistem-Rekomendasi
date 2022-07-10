import requests
import numpy as np
import tensorflow as tf
from keras.models import load_model
from flask import json
from app import config

# Load crop recommendation model
crop_recommendation = load_model('app/data/models/model_crop_recommendation.h5')

# Cast numeric label back to wordish prediction
def recommendation_label(prediction):
  result = np.argmax(prediction)

  with open('app/data/labels/dict_crop_recommendation.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == value:
      return key

# Normalize input range
def normalization(array_parameter):
  # Value is retrieved from the df.describe()
  min_val = [0, 5, 5, 8.825675, 14.258040, 3.504752, 20.211267]
  max_val = [140, 145, 205, 43.675493, 99.981876, 9.935091, 298.560117]

  for i in range(len(array_parameter[0])):
    array_parameter[0][i] = (array_parameter[0][i] - min_val[i]) / (max_val[i] - min_val[i])

  np_scaled = np.array(array_parameter)
  return np_scaled

# Fetch weather API
def weather_fetch(city_name):
  WEATHER_API = config.BASE_URL + city_name + ',id' + '&appid=' + config.API_KEY

  weather = requests.get(WEATHER_API)
  response_weather = weather.json()

  if response_weather['cod'] != '404':
    main = response_weather['main']
    temperature = round((main['temp'] - 273.15), 2)
    humidity = main['humidity']
    return temperature, humidity
  else:
    return None

# Load crop disease model
plant_disease = load_model('app/data/models/model_plant_disease.h5')

def disease_label(result):
  with open('app/data/labels/dict_plant_disease.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == key:
      return value

# Files allowed to upload
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(file_name):
  return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Image prediction
def image_prediction(img_path):
  img = tf.keras.utils.load_img(img_path, target_size=(150, 150))
  img_array = tf.keras.utils.img_to_array(img)
  img_array = tf.expand_dims(img_array, 0)
  prediction = plant_disease.predict(img_array)
  return np.argmax(prediction)