import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y), (_, _) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

titles = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B-1000', 'LSTAT', 'MEDV']

plt.figure(figsize=(12, 12))
for i in range(13):
    plt.subplot(4, 4, i + 1)
    plt.scatter(train_x[:, i], train_y, s=10)
    plt.xlabel(titles[i])
    plt.ylabel('Price($1000s)')
    plt.title(str(i + 1) + '.' + titles[i] + ' - Price')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.suptitle('各个属性与房价的关系', fontsize=20, color='red')
plt.show()
