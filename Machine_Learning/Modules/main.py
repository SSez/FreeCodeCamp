# coding=utf-8
import tensorflow as tf
import os
import nltk

print("Tensorflow version: " + tf.version.VERSION)

from tensorflow.python.client import device_lib
tf.config.experimental.list_physical_devices('GPU')
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
