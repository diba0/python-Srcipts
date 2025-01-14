import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

fig = plt.figure(facecolor='lightgrey')

plt.subplot(221)
plt.title('子标题1')
plt.subplot(222)
plt.title('子标题2', loc='left', color='b')
plt.subplot(223)
myfontdict = {'fontsize': 12, 'color': 'g', 'rotation': 30}
plt.title('子标题3', fontdict=myfontdict)
plt.subplot(224)
plt.title('子标题4', backgroundcolor='black', color='w')

plt.suptitle('全局标题', fontsize=20, color='red', backgroundcolor='yellow')

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()