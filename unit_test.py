import os

import unittest
import requests

import tensorflow as tf
import re
import numpy as np

from app import weather_fetch, normalization, recommend_predict_model, recommend_label


class AgrarisTesting(unittest.TestCase):
    def test_homepage_status_code(self):
        status_code = requests.get("http://127.0.0.1:5000/").status_code
        self.assertEqual(status_code, 200)

    def test_crop_recommendation_page_status_code(self):
        status_code = requests.get("http://127.0.0.1:5000/crop-recommendation").status_code
        self.assertEqual(status_code, 200)

    def test_weather_fetch(self):
        temperature, humidity = weather_fetch("jember")
        float_temperature = isinstance(temperature, float) or isinstance(temperature, int)
        float_humidity = isinstance(humidity, float) or isinstance(humidity, int)

        self.assertEqual(float_temperature, True)
        self.assertEqual(float_humidity, True)

    def test_weather_fetch_negative(self):
        result = weather_fetch("jembar")
        self.assertEqual(result, None)

    def test_normalization(self):
        array_test = [[90, 42, 43, 20.87974371, 82.00274423, 6.502985292000001, 202.9355362]]
        expected_result = np.array([[0.64285714, 0.26428571, 0.19, 0.34588613, 0.79026683, 0.46626364, 0.65645778]])

        result = np.isclose(expected_result, normalization(array_test), atol=.05)

        self.assertEqual(np.all(result == True), True)

    def test_normalization_diff(self):
        array_test = [[100, 42, 43, 20.87974371, 82.00274423, 6.502985292000001, 202.9355362]]
        expected_result = np.array([[0.64285714, 0.26428571, 0.19, 0.34588613, 0.79026683, 0.46626364, 0.65645778]])

        result = np.isclose(expected_result, normalization(array_test), atol=.05)

        self.assertEqual(np.all(result == True), False)

    def test_model_predict(self):
        array_test = [[90, 42, 43, 20.87974371, 82.00274423, 6.502985292000001, 202.9355362]]
        expected_result = np.array([
                                    [1.8302587e-22, 3.5993069e-16, 2.8552938e-22, 2.2512170e-19, 2.9368783e-20,
                                     1.4857074e-10, 1.2560420e-15, 2.5378998e-33, 1.4580113e-02, 0.0000000e+00,
                                     0.0000000e+00, 5.2356557e-11, 5.9933841e-30, 0.0000000e+00, 0.0000000e+00,
                                     0.0000000e+00, 1.2784132e-23, 1.6494936e-15, 3.7705900e-15, 3.6162929e-22,
                                     9.8541993e-01, 1.9517045e-17]])

        result = np.isclose(expected_result, recommend_predict_model(array_test), atol=.05)

        self.assertEqual(np.all(result == True), True)

    def test_recommend_label(self):
        array_test = np.array([
                                [1.8302587e-22, 3.5993069e-16, 2.8552938e-22, 2.2512170e-19, 2.9368783e-20,
                                 1.4857074e-10, 1.2560420e-15, 2.5378998e-33, 1.4580113e-02, 0.0000000e+00,
                                 0.0000000e+00, 5.2356557e-11, 5.9933841e-30, 0.0000000e+00, 0.0000000e+00,
                                 0.0000000e+00, 1.2784132e-23, 1.6494936e-15, 3.7705900e-15, 3.6162929e-22,
                                 9.8541993e-01, 1.9517045e-17]])

        self.assertEqual(recommend_label(array_test), "Padi")

    def test_send_request(self):
        answer = {
            "nitrogen": 60,
            "phosphorous": 55,
            "potassium": 44,
            "city": "surabaya",
            "ph": 7,
            "rainfall": 226
        }

        status_code = requests.post("http://127.0.0.1:5000/predict-crop-recommendation", data=answer)

        self.assertEqual(re.findall(r"""<span class="fw-bold">(\w+)</span>""", status_code.text)[0], "Padi"
                                                                                                     "")


if __name__ == '__main__':

    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

    unittest.main()
