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
value1 = [value1]
value2 = [value2]
value3 = [value3]


c = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="2009", max_=150000),
            opts.RadarIndicatorItem(name="2010", max_=150000),
            opts.RadarIndicatorItem(name="2011", max_=150000),
            opts.RadarIndicatorItem(name="2012", max_=150000),
            opts.RadarIndicatorItem(name="2013", max_=150000),
            opts.RadarIndicatorItem(name="2014", max_=150000),
            opts.RadarIndicatorItem(name="2015", max_=150000),
            opts.RadarIndicatorItem(name="2016", max_=150000),
            opts.RadarIndicatorItem(name="2017", max_=150000),
            opts.RadarIndicatorItem(name="2018", max_=150000),
        ]
    )
    .add("0-14岁", value1,color='#009999')
    .add("15-64岁", value2,color='#ff0000')
    .add("65岁以上", value3,color='#9fee00')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="各年龄段人口分布", subtitle="2009-2018年"))
)
c.render("radar.html")