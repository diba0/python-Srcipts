import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Load MNIST data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print('x_train:', x_train.shape, x_train.dtype)
print('y_train:', y_train.shape, y_train.dtype)
print('x_train:', len(x_train))
print('x_test:', len(x_test))
print('x_train[0]:', x_train[0])

# Display the first image in training data
for i in range(4):
    num =np.random.randint(0, len(x_train))
    plt.subplot(1, 4, i+1)
    plt.imshow(x_train[num], cmap='gray')
    plt.title("Class {}".format(y_train[num]))
    
plt.show()