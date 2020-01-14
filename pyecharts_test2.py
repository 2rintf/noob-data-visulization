from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Radar, Line,PictorialBar,Grid
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector, Faker
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = pd.read_excel('data/age_data.xls')
label = data.columns.tolist()
label = label[1:]
print(label)
print(data.loc[0].tolist())


value1 = data.loc[1].tolist()
value1 = value1[1:]
value2 = data.loc[2].tolist()
value2 = value2[1:]
value3 = data.loc[3].tolist()
value3 = value3[1:]

print(value1,value2,value3)
# value1 = [value1]
# value2 = [value2]
# value3 = [value3]


# c = (
#     Radar()
#     .add_schema(
#         schema=[
#             opts.RadarIndicatorItem(name="2009", max_=150000),
#             opts.RadarIndicatorItem(name="2010", max_=150000),
#             opts.RadarIndicatorItem(name="2011", max_=150000),
#             opts.RadarIndicatorItem(name="2012", max_=150000),
#             opts.RadarIndicatorItem(name="2013", max_=150000),
#             opts.RadarIndicatorItem(name="2014", max_=150000),
#             opts.RadarIndicatorItem(name="2015", max_=150000),
#             opts.RadarIndicatorItem(name="2016", max_=150000),
#             opts.RadarIndicatorItem(name="2017", max_=150000),
#             opts.RadarIndicatorItem(name="2018", max_=150000),
#         ]
#     )
#     .add("0-14岁", value1,color='#f9713c')
#     .add("15-64岁", value2,color='#b3e4a1')
#     .add("65岁以上", value3)
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(title_opts=opts.TitleOpts(title="各年龄段人口分布", subtitle="2009-2018年"))
# )
# c.render()

value1 = value1[::-1]
value2 = value2[::-1]
value3 = value3[::-1]
label = label[::-1]

page = Page()

c=(
    Bar()
    .add_xaxis(label)
    .add_yaxis("0-14岁", value1)
    .add_yaxis("15-64岁", value2)
    .add_yaxis("65岁以上", value3)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="各年龄段人口分布", subtitle="2009-2018年"))
)
# c.render("bar.html")


b = (
    Line()
    .add_xaxis(label)
    .add_yaxis("0-14岁", value1,is_smooth=True)
    .add_yaxis("15-64岁", value2,is_smooth=True)
    .add_yaxis("65岁以上", value3,is_smooth=True)
    .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
            title_opts=opts.TitleOpts(title="各年龄段人口分布", subtitle="2009-2018年"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
    )
)
# b.render("line.html")

page.add(c)
page.add(b)
page.render("page.html")

# grid = (
#     Grid()
#     .add(c,grid_opts=opts.GridOpts(pos_bottom='60%'))
#     .add(b,grid_opts=opts.GridOpts(pos_top='60%'))
# )

# grid.render("grid.html")

