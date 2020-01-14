from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Radar, Line,PictorialBar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector, Faker
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = pd.read_excel('data/every_year.xls')
label = data.columns.tolist()
print(label)
label = label[1:]
label = label[::-1]
total = data.loc[0].tolist()
total = total[1:]
total = total[::-1]

male = data.loc[1].tolist()
male = male[1:]
male = male[::-1]

female = data.loc[2].tolist()
female = female[1:]
female = female[::-1]

percent_np = (np.array(male)/np.array(female))*100
percent = list(percent_np)
for i in range(0,len(percent)):
    percent[i]=round(percent[i],2)


a = (
    Bar()
    .add_xaxis(label)
    .add_yaxis("男",male,stack="stack1",color="#009e8e")
    .add_yaxis("女",female,stack="stack1",color="#ff6c00")
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            is_scale=True,
            min_ = 103.5,
            name="性别比(女=100)",
            # max_=108,
            # interval=0.2
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国男女比例"),
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            name="人口数(万人)"
            # min_=103,
            # max_=108,
            # interval=0.2
        )

        #  yaxis_opts=opts.AxisOpts
    )

)
b = (
    Line()
    .add_xaxis(label)
    .add_yaxis("性别比",percent,yaxis_index=1)
)

a.overlap(b)
a.render("每年男女比例.html")