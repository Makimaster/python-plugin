# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

import textwrap
import random
import time
import json
import os
import sys,json
qid=sys.argv[1]


chinese = {"0": "", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}
def text_r90(t):
    tmp = ""
    for char in t:
        tmp += f"{char}\n"
    return tmp

def month_to_chinese(month: str):
    # 把日期数字转成中文数字
    m = int(month)
    if m < 10:
        return chinese[month[-1]]
    elif m < 20:
        return "十" + chinese[month[-1]]
    else:
        return chinese[month[0]] + "十" + chinese[month[-1]]
def make_draw():
    return random.choice(lots_items)


def draw_info(pos):
    draw_result = dict({"pos": pos}, **lots_list[pos])
    return draw_result


def gen_pic(result):
    bg = Image.open(BG_PATH)
    pen = ImageDraw.Draw(bg)

    # 文本
    year = time.strftime("%Y")
    month = month_to_chinese(time.strftime("%m")) + "月"
    day = month_to_chinese(time.strftime("%d"))
    # 正文
    final_lots = result
    raw_question = final_lots["question"]
    segmented_question = textwrap.fill(raw_question, 9)

    l_pos = final_lots["pos"]
    l_rank = final_lots["rank"]
    # l_answer = final_lots["answer"]
    l_question = segmented_question.split("\n")
    l_info = f"第{l_pos}签\u3000\u3000{l_rank}"

    # 绘制时间
    pen.text((95, 135), year, fill="#8d7650ff", font=time_font, anchor="mm")
    pen.text((350, 135), month, fill="#8d7650ff", font=time_font, anchor="mm")
    pen.text((230, 135), day, fill="#f7f8f2ff", font=time_font, anchor="mm")

    # 绘制签的具体信息
    pen.text((350, 375), text_r90(l_info), fill="#711b0f", font=lot_font, anchor="mm")
    for m, n in enumerate(l_question):
        text_x = question_x - lot_font.size * m
        r90t = text_r90(n)
        pen.text((text_x, question_y), r90t, fill="#be0a13", font=lot_font)
    bg.save(os.path.join(FILE_PATH,'qianwen/'+str(qid)+'.png'))
    info = {
        "pos": final_lots["pos"],
        "pic": bg
    }
    return info


def gen_pic1(result):
    bg = Image.open(BG_PATH)
    pen = ImageDraw.Draw(bg)

    # 文本
    year = time.strftime("%Y")
    month = month_to_chinese(time.strftime("%m")) + "月"
    day = month_to_chinese(time.strftime("%d"))
    # 正文
    final_lots = result
    #raw_question = final_lots["question"]
    segmented_question = textwrap.fill(final_lots, 9)

    #l_pos = final_lots["pos"]
    #l_rank = final_lots["rank"]
    # l_answer = final_lots["answer"]
    l_question = segmented_question.split("\n")
    #l_info = f"第{l_pos}签\u3000\u3000{l_rank}"

    # 绘制时间
    pen.text((95, 135), year, fill="#8d7650ff", font=time_font, anchor="mm")
    pen.text((350, 135), month, fill="#8d7650ff", font=time_font, anchor="mm")
    pen.text((230, 135), day, fill="#f7f8f2ff", font=time_font, anchor="mm")

    # 绘制签的具体信息text_r90(l_info)
    pen.text((350, 375),text_r90('解签') , fill="#711b0f", font=lot_font, anchor="mm")
    for m, n in enumerate(l_question):
        text_x = question_x1 - lot_font.size * m
        r90t = text_r90(n)
        pen.text((text_x, question_y), r90t, fill="#be0a13", font=lot_font)
    bg.save(os.path.join(FILE_PATH,'jieqian/'+str(qid)+'.png'))
    
    return


class jsondb:
    def __init__(self, filepath):
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding="UTF-8") as f:
                json.dump(jsondb_template, f, ensure_ascii=False, sort_keys=True, indent=4)
        dbfile = open(filepath, "r", encoding="UTF-8")
        self.db = json.loads(dbfile.read())
        self.path = filepath
        dbfile.close()

    def add_user(self, uid):
        uid = str(uid)
        self.db[uid] = {
            "time": "",
            "pos": ""
        }

    def del_user(self, uid):
        uid = str(uid)
        del self.db[uid]

    def user_list(self):
        return list(self.db.keys())

    def save(self):
        with open(self.path, 'w+', encoding="UTF-8") as f:
            json.dump(self.db, f, ensure_ascii=False, sort_keys=True, indent=4)

    def user(self, uid):
        uid = str(uid)
        try:
            return user_info(self.db[uid])
        except KeyError:
            self.add_user(uid)
            return user_info(self.db[uid])


class user_info:
    def __init__(self, db):
        self.db = db
        self.time = db["time"]
        self.pos = db["pos"]

    def write(self, pos):
        self.db["pos"] = pos
        self.db["time"] = time.strftime("%Y-%m-%d")

def get_time():
    return time.strftime("%Y-%m-%d")

def get_pic():
    return gen_pic(draw_info(make_draw()))


FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../resrouces")
DATA_PATH=os.path.join(FILE_PATH1,"../data")
                        
DB_PATH = os.path.join(DATA_PATH,"qianwen.json")
jdb = jsondb(DB_PATH)

FONT_PATH = os.path.join(FILE_PATH,'fonts',"hanyiheiti.ttf")
if not os.path.exists(FONT_PATH):
    FONT_PATH = os.path.join(FILE_PATH,'fonts', "汉仪黑体.ttf")
LIST_PATH = os.path.join(DATA_PATH, "lots_list.json")
BG_PATH = os.path.join(FILE_PATH,'alamanc', "lots_bg.png")

with open(LIST_PATH, "r", encoding="UTF-8") as f:
    lots_list = json.loads(f.read())
    lots_items = list(lots_list.keys())


time_font = ImageFont.truetype(FONT_PATH, 30)
lot_font = ImageFont.truetype(FONT_PATH, 25)
question_x = 250
question_y = 300
question_x1 = 280
if __name__ == "__main__":
    if not os.path.exists(FILE_PATH+'/jieqian'):
        os.makedirs(FILE_PATH+'/jieqian')
    if not os.path.exists(FILE_PATH+'/qianwen'):
        os.makedirs(FILE_PATH+'/qianwen')
    path1=os.path.join(FILE_PATH,'jieqian/'+str(qid)+'.png')
    path=os.path.join(FILE_PATH,'qianwen/'+str(qid)+'.png')
    if not  os.path.exists(path):
       pos=get_pic()
       pos=pos["pos"]
       jdb.user(qid).write(pos)
       jdb.save()
       print(1)
    elif not  os.path.exists(path1):
        quser = jdb.user(qid)
        answer = draw_info(quser.pos)["answer"]
        gen_pic1(answer)
        
