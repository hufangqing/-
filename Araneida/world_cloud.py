# -- coding: utf-8 --
import pyecharts.options as opts
from pyecharts.charts import WordCloud

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://gallery.echartsjs.com/editor.html?c=xS1jMxuOVm

目前无法实现的功能:

1、暂无
"""

data = [
("朝鲜", "4772813"),
("韩国", "23246398"),
("乌兹别克斯坦", "243743"),
("吉尔吉斯斯坦", "205716"),
("哈萨克斯坦","1388479"),
("土耳其	","16671848"),
("蒙古国	","978960"),
("塞浦路斯",	"574124"),
("文莱","220245"),
("孟加拉国","2011946"),
("马尔代夫",	"184856"),
("不丹	","61076"),
("巴勒斯坦",	"619519"),
("沙特阿拉伯",	"813461"),
("约旦	","1735495"),
("印度尼西亚",	"6358808"),
("亚美尼亚",	"434398"),
("卡塔尔",	"429396"),
("阿塞拜疆",	"812816"),
("格鲁吉亚",	"1735682"),
("巴基斯坦"	,"1569076"),
("阿曼	","397846"),
("阿富汗",	"193004"),
("巴林"	,"671484"),
("科威特",	"657395"),
("伊拉克",	"2457871"),
("黎巴嫩"	,"1208681"),
("以色列"	,"4632109"),
("伊朗",	"7528961"),
("印度"	,"44429258"),
("菲律宾",	"3880229"),
("斯里兰卡",	"669893"),
("柬埔寨"	,"137620"),
("尼泊尔"	,"997346"),
("越南",	"11411679"),
("马来西亚","4780284"),
("日本",	"18967043"),
("新加坡","1837090"),
("泰国","4650919"),
("海峡群岛",	"89657"),
("马恩岛"	,"38008"),
("黑山",	"275538"),
("法罗群岛",	"34658"),
("阿尔巴尼亚",	"329017"),
("保加利亚",	"1242133"),
("摩尔多瓦"	,"569088"),
("马耳他"	,"114050"),
("斯洛伐克",	"1834215"),
("梵蒂冈	","29"),
("塞尔维亚",	"2279485"),
("直布罗陀"	,"20049"),
("列支敦士登"	,"19161"),
("波黑"	,"395850"),
("匈牙利"	,"2048547"),
("斯洛文尼亚",	"1126715"),
("波兰"	,"6176885"),
("乌克兰",	"5044941"),
("拉脱维亚"	,"899133"),
("葡萄牙"	,"5417101"),
("安道尔",	"46027"),
("捷克"	,"4040773"),
("爱尔兰",	"1655338"),
("卢森堡",	"284931"),
("圣马力诺",	"20365"),
("摩纳哥",	"14375"),
("冰岛"	,"204717"),
("白俄罗斯",	"994037"),
("立陶宛",	"1218327"),
("荷兰"	,"8386307"),
("爱沙尼亚",	"597759"),
("丹麦",	"3091962"),
("罗马尼亚",	"3219354"),
("北马其顿",	"340341"),
("挪威",	"1460011"),
("希腊"	,"4762827"),
("瑞士",	"4025870"),
("克罗地亚","	1213658"),
("奥地利	","4908274"),
("比利时",	"4482315"),
("西班牙",	"13342530"),
("瑞典"	,"2564423"),
("俄罗斯",	"19528969"),
("英国"	,"23492875"),
("意大利",	"21845943"),
("芬兰",	"1258798"),
("德国"	,"32095854"),
("法国",	"34509961"),
("莱索托","34206"),
("科摩罗",	"8450"),
("圣多美和普林西比",	"6153"),
("南苏丹",	"17823"),
("马拉维",	"87856"),
("布隆迪",	"49258"),
("塞拉利昂",	"7747"),
("博茨瓦纳",	"325864"),
("几内亚比绍",	"8491"),
("马里"	,"31365"),
("利比亚",	"506790"),
("莫桑比克",	"230076"),
("厄立特里亚"	,"10154"),
("乌干达"	,"169396"),
("安哥拉"	,"102636"),
("马达加斯加",	"66626"),
("津巴布韦",	"256708"),
("佛得角",	"62310"),
("尼日尔",	"9329"),
("乍得",	"7538"),
("毛里求斯","	40178"),
("赞比亚",	"332822"),
("吉布提",	"15690"),
("冈比亚",	"12311"),
("贝宁"	,"27490"),
("索马里	","27020"),
("坦桑尼亚",	"38712"),
("利比里亚"	,"7835"),
("马约特	","40004"),
("刚果（布）","	24837"),
("中非共和国",	"14862"),
("塞舌尔",	"46081"),
("赤道几内亚",	"16950"),
("纳米比亚"	,"169253"),
("卢旺达"	,"132427"),
("斯威士兰",	"73361"),
("毛里塔尼亚",	"62762"),
("苏丹"	,"63228"),
("几内亚",	"37470"),
("埃塞俄比亚",	"493180"),
("肯尼亚	","338170"),
("加蓬	","48649"),
("加纳	","168580"),
("留尼汪岛",	"456141"),
("科特迪瓦"	,"86695"),
("刚果（金）",	"92634"),
("布基纳法索",	"21128"),
("多哥	","38465"),
("喀麦隆",	"121652"),
("南非"	,"4011657"),
("突尼斯",	"1143788"),
("塞内加尔",	"88082"),
("摩洛哥",	"1264388"),
("尼日利亚",	"263526"),
("埃及"	,"515645"),
("阿尔及利亚",	"270272"),
("图瓦卢",	"20"),
("瑙鲁共和国",	"4611"),
("纽埃","70"),
("库克群岛",	"6265"),
("基里巴斯",	"3430"),
("汤加王国",	"15235"),
("帕劳共和国",	"5348"),
("密克罗尼西亚",	"7326"),
("萨摩亚独立国",	"15767"),
("瓦努阿图共和国","11793"),
("马绍尔群岛",	"15007"),
("瓦利斯和富图纳群岛",	"761"),
("所罗门群岛",	"21544"),
("巴布亚新几内亚",	"44880"),
("新喀里多尼亚",	"73798"),
("斐济",	"68153"),
("法属波利尼西亚",	"76439"),
("新西兰",	"1740840"),
("澳大利亚",	"10031149"),
("圣皮埃尔",	"3131"),
("百慕大"	,"17785"),
("英属维尔京群岛","7291"),
("安圭拉	","3837"),
("格林纳达"	,"19289"),
("圣基茨和尼维斯",	"6509"),
("特克斯和凯科斯群岛",	"6359"),
("伯利兹",	"68238"),
("多米尼克",	"14852"),
("蒙特塞拉特","	1145"),
("海地",	"33381"),
("萨尔瓦多",	"201785"),
("尼加拉瓜",	"18491"),
("巴巴多斯",	"100973"),
("格陵兰岛",	"11971"),
("巴哈马"	,"37059"),
("瓜德罗普",	"191997"),
("开曼群岛",	"30057"),
("阿鲁巴	","42792"),
("库拉索	","45127"),
("圣卢西亚"	,"28775"),
("圣文森特和格林纳丁斯",	"7112"),
("安提瓜和巴布达	","8974"),
("危地马拉	","1100437"),
("特立尼达和多巴哥",	"178964"),
("古巴"	,"1110497"),
("洪都拉斯"	,"453443"),
("圣马丁岛"	,"10836"),
("圣巴泰勒米岛",	"5263"),
("牙买加	","149763"),
("巴拿马	","978181"),
("马提尼克	","218764"),
("哥斯达黎加",	"1049554"),
("多米尼加	","638500"),
("墨西哥	","7021598"),
("加拿大",	"4158491"),
("美国	","96149016"),
("马尔维纳斯群岛",	"1886"),
("圭亚那合作共和国"	,"71005"),
("苏里南",	"979160"),
("委内瑞拉",	"542397"),
("玻利维亚"	,"1101652"),
("法属圭亚那","93586"),
("巴拉圭",	"715162"),
("哥伦比亚",	"6299595"),
("秘鲁"	,"4102641"),
("阿根廷",	"9678225"),
("智利",	"4502674"),
("厄瓜多尔"	,"995147"),
("巴西"	,"34414011"),

]


(
    WordCloud()
    .add(series_name="世界疫情词云图", data_pair=data, word_size_range=[10, 130])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="世界疫情词云图（累计确诊）", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("世界疫情词云图.html")
)
