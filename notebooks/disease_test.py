# Import all library
import numpy as np
import tensorflow as tf
import json
import os
from PIL import Image

# Function to load model by using tensorflow
def load_model():
  model = tf.keras.models.load_model('models/best_model_plant_disease.h5')
  return model

# Function to predict image
def predict_image(path):
  img = tf.keras.utils.load_img(
    path, target_size=(150, 150)
  )

  img_array = tf.keras.utils.img_to_array(img)
  img_array = tf.expand_dims(img_array, 0)

  predictions = model.predict(img_array)
  score = tf.nn.softmax(predictions[0])

  return np.argmax(predictions)

# Function to cast numeric label back to wordish prediction
def cast_label(result):
  with open('disease_dic.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == key:
      return value

# LINK STARTTT
if __name__ == "__main__":
  model = load_model()
  absolute_path = input("Input path of the image: ")
  result = predict_image(absolute_path)
  last_result = cast_label(result)
  print("Your plant's disease is: {}".format(last_result))