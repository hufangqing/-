# -- coding: utf-8 --
# import openpyxl
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt   # 绘制图像的模块
# import numpy as np
# from PIL import Image
# # 与即时显示图片相关的模块
# '''
# import matplotlib.pyplot as plt   # 绘制图像的模块
# import numpy as np
# from PIL import Image
# '''
#
# # 读取数据
# wb = openpyxl.load_workbook('data.xlsx')
# sheet_names = wb.sheetnames
#
# frequency_out = {}
# for each in sheet_names:
#     if '洲' in each:
#         ws = wb[each]
#         for row in ws.values:
#             if row[1] == "累计确诊":
#                 pass
#             else:
#                 frequency_out[row[0]] = float(row[1])
#     else:
#         pass
#
#
# # 以省份的确诊病例总数代表其出现的频率
# frequency_in = {}
# ws = wb['国内疫情']
# for row in ws.values:
#     if row[1] == "累计确诊":
#         pass
#     else:
#         frequency_in[row[0]] = float(row[1])
#
# def generate_pic(frequency,name):
#     # 这里可以事先准备一张图片，可以用作背景
#     background_image = np.array(Image.open('bindu.jpg'))
#     wordcloud = WordCloud(font_path="C:/Windows/Fonts/SIMLI.TTF",
#                           background_color = "white",
#                           mask=background_image,
#                           width=1920, height=1080
#                           )
#     # 按照确诊病例数目生成词云
#     wordcloud.generate_from_frequencies(frequency)
#     wordcloud.to_file('%s.png'%name)
#
#     # 展示图片
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.show()
#
# # 调用函数
# generate_pic(frequency_in,'国内疫情')
# generate_pic(frequency_out,'国外疫情')
#




# import openpyxl
# from wordcloud import WordCloud
#
# wb = openpyxl.load_workbook('data.xlsx')
# sheet_names = wb.sheetnames
#
# frequency_out = {}
# for each in sheet_names:
#     if '洲' in each:
#         ws = wb[each]
#         for row in ws.values:
#             if row[1] == "累计确诊":
#                 pass
#             else:
#                 frequency_out[row[0]] = float(row[1])
#     else:
#         pass
#
#
# # 以省份的确诊病例总数代表其出现的频率
# frequency_in = {}
# ws = wb['国内疫情']
# for row in ws.values:
#     if row[1] == "累计确诊":
#         pass
#     else:
#         frequency_in[row[0]] = float(row[1])
#
# def generate_pic(frequency,name):
#     wordcloud = WordCloud(font_path="STXINGKA.TTF",
#                           background_color = "#FF0000",
#                           width=1920, height=1080
#                           )
#     # 按照确诊病例数目生成词云
#     wordcloud.generate_from_frequencies(frequency)
#     wordcloud.to_file('%s.png'%name)
#
# # 调用函数
# generate_pic(frequency_in,'国内疫情')
# generate_pic(frequency_out,'国外疫情')


import json
from pyecharts import options as opts
from pyecharts.charts import WordCloud

words = [
    ("西藏", 713),
    ("澳门", 793),
    ("青海", 109),
    ("台湾", 527344),
    ("香港", 384229),
    ("贵州", 149),
    ("吉林", 40311),
    ("新疆", 1126),
    ("宁夏", 86),
    ("内蒙古", 2382),
    ("甘肃", 1346),
    ("天津", 2202),
    ("山西", 469),
    ("辽宁", 1804),
    ("黑龙江", 3074),
    ("南海", 8767),
    ("河北", 2016),
    ("陕西", 3669),
    ("云南", 2277),
    ("广西", 2254),
    ("福建", 4244),
    ("上海", 63830),
    ("北京", 3975),
    ("江苏", 2352),
    ("四川", 3421),
    ("山东", 2955),
    ("江西", 1455),
    ("重庆", 952),
    ("安徽", 1312),
    ("湖南", 1487),
    ("河南", 3163),
    ("广东", 8104),
    ("浙江", 3352),
    ("湖北", 68423),

]

c = (
    WordCloud()
    .add(
        "",
        words,
        word_size_range=[20, 180],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情词云图（累计确诊）"))
    .render("中国疫情词云图.html")
)



