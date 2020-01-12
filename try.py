import matplotlib.pyplot as plt

# 连线
s=[1,4,9,16,25]
plt.plot([1,2,3,4,5],[1,1,1,2,2],linewidth=5)
plt.show()


# 散点图
plt.scatter([1,2,3,4,5],[1,1,1,2,2])
plt.title("test pic",fontsize=24)
plt.xlabel("X")
plt.ylabel("Y")
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()


#简单例子 (python的语法糖可真甜嗷，呕)
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# print(x_values)
plt.scatter(x_values,y_values,c='green',edgecolors='none',s=10)
# plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=10)
plt.axis([0,1100,0,1100000])   # 给x,y轴设置取值范围
plt.show()

#颜色映射(colormap)
x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,edgecolor='none', s=40)
plt.savefig('try.png')
plt.show()


#保存(第二个参数决定是否保留图表多余的空白区域)
#! 要在plt.show()之前 
# plt.savefig('try.png',bbox_inches='tight')
plt.savefig('try.jpg')


