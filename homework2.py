import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = pd.read_excel('data/every_year.xls')
label = data.columns.tolist()
print(label)

data_name = data['指标'].tolist()
print(data_name)
data_name = data_name[0:4]
print(data_name)

time = label[1:]
print(time)

x = data.loc[0].tolist()
print(x)
print(x[::-1])# 反转
# print(data.loc[0].tolist())
xValues = time
xValues = xValues[::-1]
yValues = x[1:]
yValues = yValues[::-1]

plt.bar(xValues,yValues,color='b',alpha=0.5)
plt.plot(xValues,yValues,color='r',alpha=0.5)
plt.xlabel('年份')
plt.ylabel('总人口(万人)')
plt.ylim([yValues[0]-1000,yValues[-1]+1000])
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'both')  
# plt.legend()
plt.title('2009-2018年中国总人口数')

plt.savefig('中国总人口数.jpg',dpi=500)
plt.show()


male = data.loc[1].tolist()
female = data.loc[2].tolist()

male = male[1:]
female = female[1:]
male = male[::-1]
female = female[::-1]
male_np = np.array(male)
female_np = np.array(female)
percent_np = male_np/female_np*100
percent = percent_np.tolist()
print(percent)
xValues = time[::-1]
yValues = percent
plt.plot(xValues,yValues)
plt.xlabel('年份')
plt.ylabel('性别比(女=100)')
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'both')  
plt.title('2009-2018年中国性别比')
plt.text(5.5,105.8,'注：性别比正常范围为104~107')
for i in range(0,len(xValues)):
    plt.text(i,yValues[i],round(yValues[i],2))
plt.xlim([-1,10])
plt.savefig('性别比.jpg',dpi=500)
plt.show()