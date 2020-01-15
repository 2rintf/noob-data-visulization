from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Radar, Line,PictorialBar
from pyecharts.faker import Collector, Faker
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType

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
a=(
    PictorialBar()
    .add_xaxis(xValues[::-1])
    .add_yaxis(
        "",
        yValues_total[::-1],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=10,
        symbol_repeat="fixed",
        symbol_offset=[2, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各地区人口数",subtitle="第六次人口普查"),
        xaxis_opts=opts.AxisOpts(is_show=True,name="人口数"),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0.5)
            ),
        ),
    )
)

a.render("各省份人口数.html")