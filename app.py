# Import library
from flask import Flask, render_template

# Create flask app
app = Flask(__name__)

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

# Run flask app
if __name__ == '__main__':
  app.run(debug=True)