# Import library
import numpy as np
import requests
import tensorflow as tf
from flask import Flask, render_template, request, json, Markup
from keras.models import load_model

# Create flask app
app = Flask(__name__)

# Load crop recommendation model
crop_recommendation_model = load_model('models/model_dir/best_model_crop_recommendation.h5')

# Load crop disease model
crop_disease_model = load_model('models/model_dir/best_model_plant_disease.h5')

# Cast numeric label back to wordish prediction
def recommend_label(prediction):
  result = np.argmax(prediction)

  with open('models/label_dir/recommend_dic.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == value:
      return key

def disease_label(result):

  with open('models/label_dir/disease_dic.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == key:
      label_value = value

  with open('models/label_dir/disease_dic_desc.json', 'r') as file:
    labels = json.load(file)

  for key, value in labels.items():
    if str(result) == key:
      desc_value = value
  
  return label_value, desc_value

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
  base_url = 'https://api.openweathermap.org/data/2.5/weather?q='
  api_key = '1661559d236944b41319e5fe4c287b2e'
  city_url = base_url + city_name + ',id' + '&appid=' + api_key

  response = requests.get(city_url)
  response_json = response.json()

  if response_json['cod'] != '404':
    main = response_json['main']
    temperature = round((main['temp'] - 273.15), 2)
    humidity = main['humidity']
    return temperature, humidity
  else:
    return None

# Allowed file upload
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Predict image
def predict_image(img_path):
  img = tf.keras.utils.load_img(img_path, target_size=(150, 150))
  img_array = tf.keras.utils.img_to_array(img)
  img_array = tf.expand_dims(img_array, 0)
  predictions = crop_disease_model.predict(img_array)
  return np.argmax(predictions)

# Render home page
@app.route('/')
def home():
  return render_template('index.html')

# Render crop recommendation page
@app.route('/crop-recommendation')
def crop_recommendation():
  return render_template('recommend.html')

# Render crop disease page
@app.route('/crop-disease')
def crop_disease():
  return render_template('disease.html')

# Render predict crop recommendation page
@app.route('/predict-crop-recommendation', methods=['POST'])
def recommend_predict():
  N = int(request.form['nitrogen'])
  P = int(request.form['phosphorous'])
  K = int(request.form['potassium'])
  city = request.form.get('city')
  ph = float(request.form['ph'])
  rainfall = float(request.form['rainfall'])

  if weather_fetch(city) != None:
    temperature, humidity = weather_fetch(city)
    user_input = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled = normalization(user_input)
    prediction = crop_recommendation_model.predict(scaled)
    result = recommend_label(prediction)
    return render_template('recommend-predict.html', prediction=result)
  else:
    return render_template('recommend.html')

# Render predict crop disease page
@app.route('/predict-crop-disease', methods=['POST'])
def disease_predict():
  file = request.files['file']
  if file and allowed_file(file.filename):
    img_path = 'static/uploads/' + file.filename
    file.save(img_path)
    prediction = predict_image(img_path)
    result, desc = disease_label(prediction)
    asd = Markup(desc)
    return render_template('disease-predict.html', prediction=result, description=asd)
  else:
    return render_template('disease.html')

# Run flask app
if __name__ == '__main__':
  app.run(debug=True)