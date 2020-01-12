import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = pd.read_excel('data/1.xls')
# print(data)
# print(data[7:11])
label = data.columns.tolist()
print(label)
total_popu = data['合计']
total_popu_male = data['男']
total_popu_female = data['女']
area = data['地区']


# 处理数据中的空格
area = area.str.replace(" ","")
print(area)


# area_list = np.array(area.values)
# popu_list = np.array(total_popu.values)

# print(test)

# 合成一个二维列表
test = zip(area.values,total_popu.values)
test = [list(i) for i in test] # 关键操作
# 按人口数排序，从高到低
test = sorted(test,key=(lambda x: x[1]),reverse=True)
print(test)
area_test = [i[0] for i in test]
popu_test = [i[1] for i in test]
# area = area_test[4:]
# popu = popu_test[4:]



# 总人口图
xValues = area_test[4:]
yValues_total = popu_test[4:]
plt.title('第六次人口普查--中国各地区总人口数')
plt.barh(xValues,yValues_total,color=['b','r','g','y','c','m','y','k','c','g'],alpha=0.7)
plt.tick_params(labelsize=8,axis='y')
plt.ylabel('地区')
plt.xlabel('人口数')
# plt.legend()# 图例
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'both')  
plt.savefig('各地区人口数.jpg',dpi=500)
plt.show()


# 性别比例图——总
maleValues = total_popu_male[4]
femaleValues = total_popu_female[4]
plt.title('第六次人口普查--中国男女比例')
plt.pie([maleValues,femaleValues],labels=['男','女'],autopct='%1.1f%%',
        startangle=90,shadow=True)
plt.legend()
plt.savefig('人口普查男女比例.jpg',dpi=500)
plt.show()




