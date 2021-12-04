# Modelling Crop Recommendation

### Attention: Unzip the model before starting the testing files!

## Summary

Agraris' supporting feature is plant disease classification which is able to predict whether the target is infected by one of the common diseases for plants or not. This model will take an input of image, and classify the image into one of 38 class.

This repository is mainly consisted of 2 files:

- tf_based_model.ipynb (main model file, place to make model)
- tf_test_with_explanation.ipynb  (used to do testing)

------



## How to make the model?


### Data Preparation for Modelling

1. **Augment** the picture to **get a better accuracy** from small data pool (this process has been done before, so in this code there is no augmentation process)
2. **Cast** the image into a **TensorFlow vector** to be processed using **keras.image_dataset_from_directory** , as the image has been augmented before.


### Modelling Process

3. Define the model. In this scoop, the model uses **11 layers of Keras' layers**. The activation function used in the model is **ReLu** for most of the layers, as the ReLU activation function is one of the best activation function.

   The last activation function is different (**softmax**) is used to do **multi-class classification.**

4. Define the callbacks that are going to be used. In this case, there are two callbacks that are used in this model. The first callback is the Reminder callback, which is used to get the notification that the accuracy has reached the threshold of the accuracy (in this scoop is 0.99). This callback is used to flag the "good" model, and differ it from the others.

5. Define the second callback (checkpointCB). This checkpoint is used to save the best model that this iteration has ever had. The model is stored at the model folder. This callback is used to get the best model for the prediction later, or just to simply save the model as a .h5 file to be able to be reused.

6. Compile the model. The loss used in this optimization is the sparse categorical cross-entropy (this loss is optimized for multi-class classification). To fit this model better, the Adam optimizer is used with the accuracy as the metric.

7. Fit the model with the epoch of 10.

    
### Evaluation

8. Plot the accuracy of the model in the epoch. The plot is for accuracy of both the train set and the test set. After plotting, check the graph. Does the accuracy continue to increase or keep decreasing? If it continues to increase, then the model is well-fit.
9. Plot the loss of the model in the epoch. As the opposite of accuracy, the plot is for loss of both the train set and the test set should decrease in each epoch. After plotting, check the graph. Does the loss continue to decrease or keep increasing? If it continues to decrease, then the model is well-fit.

### Model-saving

10. The last model is the best model among the epochs, so the last model is saved into a .hdf5 file to be able to be retrained, or just to load.

------

##  How to use the model?

To check the eligibility of this model by our own input, and to be able to manipulate the model, this is the right place for testing. To to this, I provided guideline to do the testing process.

The testing process can be done in either tf_test_with_explanation.ipynb (if you want to see throughout the whole documentation) or just want to try the execution (tf_test.py).



Below is the how to use this testing model step by step:

1. Load the library
2. Run the main function to load the model
3. Follow the instruction
4. Input the image link (must be a link to the image!)
5. Get the classification result

------

## How does it work?

1. Get the user input
2. Process the user input link, process the image
3. Cast the label
4. Give the user the result
