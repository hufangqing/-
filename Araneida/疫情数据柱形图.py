# -- coding: utf-8 --
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(['中国','日本','德国','美国','印度','英国','韩国'])
    .add_yaxis("累计确诊",[5000000,11510000,30330000,92330000,43910000,23210000,19240000])
    .add_yaxis("累计死亡",[23000,31000,143000,1052000,526000,182000,24000])
    .set_global_opts(
        title_opts={"text": "熟悉国家疫情柱形图", "subtext": "累计确诊/累计死亡"}
    )
    .render("熟悉国家疫情柱状图.html")
)

