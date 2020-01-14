from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Radar, Line,PictorialBar,Geo
from pyecharts.faker import Collector, Faker
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType,ChartType


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = pd.read_excel('data/1.xls')
label = data.columns.tolist()
# print(label)
area = data['地区']
area = area.str.replace(" ","")
percent = data['性别比']
area = area[4:]
percent = percent[4:]
percent_np = np.array(percent)

total_popu = data['合计']
total_popu = total_popu[4:]
total_popu_male = data['男']
total_popu_male = total_popu_male[4:]
total_popu_female = data['女']
total_popu_female = total_popu_female[4:]

# 总人口归一化
total_np = np.array(total_popu)
max = np.max(total_np)
temp = total_np/max*100
print(temp)
total_norm = temp.tolist()
print(total_norm)





# needed = [list(z) for z in zip(area,percent)]

needed = [list(z) for z in zip(area,total_norm)]
print(needed)

needed_male = [list(z) for z in zip(area,total_popu_male)]
needed_female = [list(z) for z in zip(area,total_popu_female)]


geo = (
    Geo()
    .add_schema(maptype="china")
    .add("人口密集程度",needed,type_=ChartType.HEATMAP)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="中国各地区人口热力图",subtitle="基于第六次人口普查"),
    )
)
# geo.render("地图形式展示各地区人口数.html")

geo2 = (
    Geo()
    .add_schema(maptype="china")
    .add("男",needed_male)
    .add("女",needed_female)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_ = np.max(np.array(total_popu_male))),
        title_opts=opts.TitleOpts(title="中国各地区男女人口数量分布图",subtitle="基于第六次人口普查"),
    )
)

page = Page()
page.add(geo)
page.add(geo2)
page.render("地图形式展示各地区人口数.html")