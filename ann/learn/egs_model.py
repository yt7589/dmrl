#
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import tensorflow.keras as tfk
import tensorflow.keras.layers as tfkl

class EgsModel(tfk.Model):
    def  __init__(self):
        super(EgsModel, self).__init__()
        self.conv1 = tfkl.Conv2D(32, 3, activation='relu')
        self.flatten = tfkl.Flatten()
        self.d1 = tfkl.Dense(128, activation='relu')
        self.d2 = tfkl.Dense(10, activation='softmax')

    def call(self, x):
        x = self.conv1(x)
        x = self.flatten(x)
        x = self.d1(x)
        return self.d2(x)
