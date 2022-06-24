# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from genshincalendar import genshincalendar
import os
import json
import random
import base64
import time

FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../resrouces")
FONT_PATH = os.path.join(FILE_PATH, 'fonts',"hanyiheiti.ttf")
if not os.path.exists(FONT_PATH):
    FONT_PATH = os.path.join(FILE_PATH,'fonts',"汉仪黑体.ttf")

BG_PATH = os.path.join(FILE_PATH,'alamanc',"back.png")
DATA_PATH=os.path.join(FILE_PATH1,"../data")
LIST_PATH = os.path.join(DATA_PATH,  "almanac_list.json")
data = {}  # config.json里的数据

almanac_data = {
    # 生成的黄历base64字符串和黄历更新日期
    "date": "",
    "almanac_base64_str": ""
}

chinese = {"0": "", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}


def month_to_chinese(month: str):
    # 把日期数字转成中文数字
    m = int(month)
    if m < 10:
        return chinese[month[-1]]
    elif m < 20:
        return "十" + chinese[month[-1]]
    else:
        return chinese[month[0]] + "十" + chinese[month[-1]]


def load_data():
    # 载入config.json文件的数据
    global data
    with open(LIST_PATH, 'r', encoding='UTF-8') as f:
        data = json.load(f)

    almanac_data["date"] = ""
    almanac_data["almanac_base64_str"] = ""


load_data()


def seed_random_list(seed: str, l: list):
    # 使用随机种子随机选择列表中的元素，相同的种子和列表将返回同样的输出
    seed = seed + str(l)
    random.seed(seed)
    index = random.random() * len(l)
    return l[int(index)]


def generate_almanac():
    # 生成黄历图片，然后转换成base64保存到 almanac_data["almanac_base64_str"]

    seed = time.strftime("%Y-%m-%d")
    offset = 1
    today_luck = []
    l = list(data.keys())

    while len(today_luck) < 6:
        # 随机6个不同的运势放到 today_luck
        r = seed_random_list(str(offset) + seed, l)
        if r in today_luck:
            offset += 1
        else:
            today_luck.append(r)

    back = Image.open(BG_PATH)

    year = time.strftime("%Y")
    month = month_to_chinese(time.strftime("%m")) + "月"
    day = month_to_chinese(time.strftime("%d"))

    draw = ImageDraw.Draw(back)
    draw.text((118, 165), year, fill="#8d7650ff", font=ImageFont.truetype(FONT_PATH, size=30), anchor="mm",
              align="center")
    draw.text((260, 165), day, fill="#f7f8f2ff", font=ImageFont.truetype(FONT_PATH, size=35), anchor="mm",
              align="center")
    draw.text((410, 165), month, fill="#8d7650ff", font=ImageFont.truetype(FONT_PATH, size=30), anchor="mm",
              align="center")

    buff = Image.new("RGBA", (325, 160))
    debuff = Image.new("RGBA", (325, 160))

    buff_draw = ImageDraw.Draw(buff)
    debuff_draw = ImageDraw.Draw(debuff)

    for i in range(3):
        buff_name = today_luck[i]
        debuff_name = today_luck[(i + 3)]

        buff_effect = seed_random_list(seed, data[buff_name]["buff"])
        debuff_effect = seed_random_list(seed, data[debuff_name]["debuff"])

        buff_draw.text((0, i * 53), buff_name, fill="#756141ff", font=ImageFont.truetype(FONT_PATH, size=25))
        debuff_draw.text((0, i * 53), debuff_name, fill="#756141ff", font=ImageFont.truetype(FONT_PATH, size=25))

        buff_draw.text((0, i * 53 + 28), buff_effect, fill="#b5b3acff", font=ImageFont.truetype(FONT_PATH, size=19))
        debuff_draw.text((0, i * 53 + 28), debuff_effect, fill="#b5b3acff", font=ImageFont.truetype(FONT_PATH, size=19))

    back.paste(buff, (150, 230), buff)
    back.paste(debuff, (150, 400), debuff)

    bio = BytesIO()
    back.save(bio, format='PNG')
    im=genshincalendar.calendar()
    x1=int(back.size[0]*im.size[1]/back.size[1])
    back=back.resize((x1,im.size[1]))
    width=im.size[0]+back.size[0]+10
    height=max(back.size[1],im.size[1])
    img=Image.new('RGBA', (width, height), (255, 255, 255, 0))
    img.paste(back,(0,0))
    img.paste(im,(back.size[0],0))
    img.save(os.path.join(FILE_PATH,"qianwen/黄历.png"))
    base64_str = base64.b64encode(bio.getvalue()).decode()

    almanac_data["date"] = time.strftime("%Y-%m-%d")
    almanac_data["almanac_base64_str"] = 'base64://' + base64_str


def get_almanac_base64_str():
    # if almanac_data["date"] == time.strftime("%Y-%m-%d"):
    #     return almanac_data["almanac_base64_str"]
    # else:
    #     generate_almanac()
    #     return almanac_data["almanac_base64_str"]
    generate_almanac()
    return almanac_data["almanac_base64_str"]
if not os.path.exists(FILE_PATH+'/jieqian'):
    os.makedirs(FILE_PATH+'/jieqian')
if not os.path.exists(FILE_PATH+'/qianwen'):
    os.makedirs(FILE_PATH+'/qianwen')
a=get_almanac_base64_str()
