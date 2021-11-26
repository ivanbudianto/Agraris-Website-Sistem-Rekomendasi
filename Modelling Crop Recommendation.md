# Modelling Crop Recommendation



## Summary

Agraris is a model to classify the land based on the user's input to get the best crop for the land. By using this model, we can get the best kind of crop to be cultivated in the user's respective land to maximize the productivity of the land.

This repository is mainly consisted of 2 files:

- tf_based_model.ipynb (main model file, place to make model)
- tf_test_tutorial.ipynb  (used to do testing)

------



## How to make the model?

### Data Pre-processing

1. Load the dataset from the dataset folder from **"dataset/Crop_recommendation.csv"** using pandas.

2. Get the description of the data statistically to find the overall value of the data by using **describe()**.

3. Encode the labels to integer value (as a string is a little bit complicated to be used as it is). After it is encoded as integer, a **JSON** file is made to **keep track of the encoded labels**. So, the **dictionary** of **key-value of string-integer pair** is stored in a file named **"dataset/labelEncoder_dict.json"**.

4. **Scale** the data (as the data's range are too various, and it will be a hard job for the system to directly process the data into the model) using **MinMaxScaler of Sci-Kit Learn**. The scaled data are applied to the dataframe for visualization purpose.

   **Note: The scaled data are only the features. Labels are NOT scaled.**



### Data Preparation for Modelling

5. Separate/select the label, and the feature. As the label is located in the last index (the 7th index), and put the other column into the features columns.

6. Cast the 22 labels into a simplified 22 columns of binary number, as binary numbers are way easier for the system to process rather than the number as it is. To do this, use the Keras' utility, the tf.keras.utils.to_categorical([array]).

7. Split and shuffle the feature and the label (X and y) into 2 different usage. In this scoop, the feature is divided as the train set and test set with the proportion of 90% train set, and the 10% as the test set.



### Modelling Process

8. Define the model. In this scoop, the model uses **4 layers** of **Keras' Dense layer**. The activation function used in the model is **ReLu** for the first 3 layers, as the ReLU activation function is one of the best activation function.

   The last activation function is different (**softmax**) is used to do **multi-class classification**.

9. Define the **callbacks** that are going to be used. In this case, there are **two callbacks** that are used in this model. The first callback is the **Reminder** callback, which is used to get the notification that the accuracy has reached the threshold of the accuracy (in this scoop is 0.99). This callback is used to flag the "good" model, and differ it from the others.

10. Define the second callback (**checkpointCB**). This checkpoint is used to save the best model that this iteration has ever had. The model is stored at the model folder. This callback is used to get the best model for the prediction later, or just to simply **save the model as a .h5 file to be able to be reused**.

11. Compile the model. The loss used in this optimization is the **categorical cross-entropy** (this loss is optimized for multi-class classification). To fit this model better, the R**oot Mean Square Propagation (RMS-Prop)** with the accuracy as the metric.

12. Fit the model with the **epoch of 200**, and the **steps per epoch is 50**.



### Evaluation

13. Plot the **accuracy** of the model in the epoch. The plot is for accuracy of **both the train set and the test set**. After plotting, check the graph. Does the accuracy continue to increase or keep decreasing? **If it continues to increase, then the model is well-fit.**

14. Plot the **loss** of the model in the epoch. As the opposite of accuracy, the plot is for loss of **both the train set and the test set** should decrease in each epoch. After plotting, check the graph. Does the loss continue to decrease or keep increasing? **If it continues to decrease, then the model is well-fit.**

------

##  How to use the model?

To check the eligibility of this model by our own input, and to be able to manipulate the model, this is the right place for testing. To to this, I provided guideline to do the testing process.

The testing process can be done in either tf_test_tutorial.ipynb (if you want to see throughout the whole documentation) or just want to try the execution (tf_test.py).



Below is the how to use this testing model step by step:

1. Load the library

2. Run the main function to load the model and print the MVP menu (still CLI based)

3. Follow the instruction. Choose 1 to input the land condition.

4. Follow the instruction for the 7 field input process. Below is the guide:

	- Input the ***\*Natrium\**** value
	- Input the ***\*Phosphorus\**** value
	- Input the ***\*Kalium\**** value
	- Input the ***\*Temperature\**** value
	- Input the ***\*Humidity\**** value
	- Input the ***\*pH\**** value
	- Input the ***\*Rainfall\**** value

5. Get the recommendation value

------

## How does it work?

1. Get the user input from **show_input_form()**.

2. Scale the user input, and cast it into the NumPy array using **normalization(user_input)**.

3. Predict the user input using the model loaded from **load_model()**. The method used is **model.predict(np_user_input_scaled)**.

4. Cast the label of the prediction using **cast_label(prediction)** to get the real readable result.
