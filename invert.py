import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

P_SIZE = np.random.randint(256)

ones = np.ones((P_SIZE, P_SIZE, 1))
rand = np.round(np.random.uniform(low=0.0, high=1.0, size=(P_SIZE, P_SIZE, 1)), 2)

ones = tf.constant(ones, dtype=tf.float16)
rand = tf.constant(rand, dtype=tf.float16)

rounded = tf.math.round(rand)

inverted = tf.math.subtract(ones, rounded)

plt.figure(figsize=(15, 15))
display_list = [rand, rounded, inverted]
title = ['Random', 'Rounded', 'Inverted']

for i in range(len(display_list)):
    plt.subplot(1, len(display_list), i+1)
    plt.title(title[i])
    plt.imshow(tf.keras.preprocessing.image.array_to_img(display_list[i]))
    plt.axis('off')
plt.show()
