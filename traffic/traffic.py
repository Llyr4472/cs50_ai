import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    """# Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])"""
    images, labels = load_data("gtsrb-small")

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    #if len(sys.argv) == 3:
    if True:
        filename = "model"#sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = []
    labels = []
    for category in os.listdir(data_dir):
        label = category
        for image in os.listdir(os.path.join(data_dir,category)):
            with open(os.path.join(data_dir,category,image)) as img:
                image = cv2.imread(img,mode="RGB")
                image = cv2.resize(image,IMG_HEIGHT,IMG_WIDTH)
                images.append(image)
                labels.append(label)
    return images, labels


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)

    model = tf.keras.Sequential()

    #convolution and pooling layers 1
    model.add(tf.keras.layers.Conv2D(32,(3,3),activation="relu",input_shape=input_shape))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(3,3)))

    #Flaten units
    model.add(tf.keras.layers.Flatten())

    #hidden layer
    model.add(tf.keras.layers.Dense(64,input_shape=input_shape, activation="relu"))

    #dropout layer
    model.add(tf.keras.layers.Dropout(0.5))

    #output layer
    model.add(tf.keras.layers.Dense(NUM_CATEGORIES-1,activation="sigmoid"))


if __name__ == "__main__":
    main()
