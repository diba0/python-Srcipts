import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

# 下载数据集
TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
train_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)

# 读取数据集
COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
df_iris = pd.read_csv(train_path, names=COLUMN_NAMES, header=0)

# 转换为数组
iris = df_iris.values   

# 画散点图

fig = plt.figure('Iris Data', figsize=(15, 3))
fig.suptitle('Anderson\'s Iris Data Set\n(Blue->Setosa, Green->Versicolor, Red->Virginica)', fontsize=20)

for i in range(4):
    for j in range(4):
        plt.subplot(4, 4, 4 * i + j + 1)

        if i == j:
            plt.text(0.3,0.5,COLUMN_NAMES[0],fontsize=15)
        else:
            plt.scatter(iris[:,j], iris[:,i], c=iris[:,4], s=20, cmap='brg')
        if i == 0:
            plt.title(COLUMN_NAMES[j])
        if j == 0:
            plt.ylabel(COLUMN_NAMES[i])

plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show() 