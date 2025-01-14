import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

n = 24
y1 = np.random.randint(27, 37, n)
y2 = np.random.randint(40, 60, n)

plt.plot(y1, label='温度', color='r', linestyle='-', linewidth=2)
plt.plot(y2, label='湿度', color='b', linestyle='--', linewidth=3)

plt.xlim(0, 23)
plt.ylim(20, 70)
plt.xlabel('小时', fontsize=12)
plt.ylabel('测量值', fontsize=12)

plt.title('24小时温湿度变化图', fontsize=16)

plt.legend(loc='upper right', fontsize=12)

plt.show()