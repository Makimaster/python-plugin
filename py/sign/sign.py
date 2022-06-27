import json,random
import sys,os
import requests
from datetime import datetime,timedelta
from image_utils import BuildImage
from pathlib import Path
from random_event import random_event
from io import BytesIO
import pytz
tz = pytz.timezone('utc')
FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../../resrouces")
if not os.path.exists(FILE_PATH+'/today_card'):
    os.makedirs(FILE_PATH+'/today_card')
SIGN_RESOURCE_PATH = Path(__file__).parent.parent.parent / "resrouces" / "sign_res"
SAVE_PATH=Path(__file__).parent.parent.parent / "resrouces" / 'today_card'
SIGN_BORDER_PATH = SIGN_RESOURCE_PATH / 'border'
SIGN_BACKGROUND_PATH = SIGN_RESOURCE_PATH / 'background'
#SIGN_BORDER_PATH.mkdir(exist_ok=True, parents=True)
#SIGN_BACKGROUND_PATH.mkdir(exist_ok=True, parents=True)
qid=sys.argv[2]
name=sys.argv[1]
DATA_PATH=Path(__file__).parent.parent.parent/"data"
NICKNAME=sys.argv[3]
lik2relation = {
    '0': '路人',
    '1': '陌生',
    '2': '初识',
    '3': '普通',
    '4': '熟悉',
    '5': '信赖',
    '6': '相知',
    '7': '厚谊',
    '8': '亲密'
}

level2attitude = {
    '0': '排斥',
    '1': '警惕',
    '2': '可以交流',
    '3': '一般',
    '4': '是个好人',
    '5': '好朋友',
    '6': '可以分享小秘密',
    '7': '喜欢',
    '8': '恋人'
}

weekdays = {
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat',
    7: 'Sun'
}

lik2level = {
    9999: '9',
    400: '8',
    270: '7',
    200: '6',
    140: '5',
    90: '4',
    50: '3',
    25: '2',
    10: '1',
    0: '0'
}

def get_level_and_next_impression(impression: float):
    if impression == 0:
        return lik2level[10], 10, 0
    keys = list(lik2level.keys())
    for i in range(len(keys)):
        if impression > keys[i]:
            return lik2level[keys[i]], keys[i - 1], keys[i]
    return lik2level[10], 10, 0

def get_user_avatar(qq: int):
    """
    说明：
        快捷获取用户头像
    参数：
        :param qq: qq号
    """
    url = f"http://q1.qlogo.cn/g?b=qq&nk={qq}&s=160"
    res=requests.get(url).content
    return res
def get_card(nickname):
    gold=info['gold']
    impression=info['impression']
    if not is_sign:
        #随机金币
        gold_add = random.randint(1, 100)
        gold+=gold_add
        #随机好感
        impression_added = random.randint(1, 100)/100
        critx2 = random.random()
        add_probability = 0
        specify_probability = 0
        if critx2 + add_probability > 0.97:
            impression_added *= 2
        elif critx2 < specify_probability:
            impression_added *= 2
        impression+=impression_added
        gift, gift_type = random_event(impression)
        if gift_type == "gold":
            gift = f"额外金币 + {gift}"
        else:
            gift += ' + 1'
        info['count']=info['count']+1
    else:
        gift=''
    ava_bk = BuildImage(140, 140, is_alpha=True)
    ava_border = BuildImage(
        140,
        140,
        background=SIGN_BORDER_PATH / "ava_border_01.png",
    )
    ava=BytesIO(get_user_avatar(qid))
    ava = BuildImage(102, 102, background=ava)
    ava.circle()
    ava_bk.paste(ava, center_type="center")
    ava_bk.paste(ava_border, alpha=True, center_type="center")

    info_img = BuildImage(250, 150, color=(255, 255, 255, 0), font_size=15)
    level, next_impression, previous_impression = get_level_and_next_impression(
        impression
    )
    info_img.text((0, 0), f"· 好感度等级：{level} [{lik2relation[level]}]")
    info_img.text((0, 20), f"· {NICKNAME}对你的态度：{level2attitude[level]}")
    info_img.text((0, 40), f"· 距离升级还差 {next_impression - impression:.2f} 好感度")

    bar_bk = BuildImage(220, 20, background=SIGN_RESOURCE_PATH / "bar_white.png")
    bar = BuildImage(220, 20, background=SIGN_RESOURCE_PATH / "bar.png")
    bar_bk.paste(
        bar,
        (
            -int(
                220
                * (
                    (next_impression - impression)
                    / (next_impression - previous_impression)
                )
            ),
            0,
        ),
        True,
    )
    font_size = 30
    if "好感度双倍加持卡" in gift:
        font_size = 20
    gift_border = BuildImage(
        270,
        100,
        background=SIGN_BORDER_PATH / "gift_border_02.png",
        font_size=font_size,
    )
    gift_border.text((0, 0), gift, center_type="center")

    bk = BuildImage(
        876,
        424,
        background=SIGN_BACKGROUND_PATH
        / random.choice(os.listdir(SIGN_BACKGROUND_PATH)),
        font_size=25,
    )
    A = BuildImage(876, 274, background=SIGN_RESOURCE_PATH / "white.png")
    line = BuildImage(2, 180, color="black")
    A.transparent(2)
    A.paste(ava_bk, (25, 80), True)
    A.paste(line, (200, 70))

    nickname_img = BuildImage(
        0,
        0,
        plain_text=nickname,
        color=(255, 255, 255, 0),
        font_size=50,
        font_color=(255, 255, 255),
    )
    if qid:
        uid = f"{qid}".rjust(12, "0")
        uid = uid[:4] + " " + uid[4:8] + " " + uid[8:]
    else:
        uid = "XXXX XXXX XXXX"
    uid_img = BuildImage(
        0,
        0,
        plain_text=f"QQ: {qid}",
        color=(255, 255, 255, 0),
        font_size=30,
        font_color=(255, 255, 255),
    )
    sign_day_img = BuildImage(
        0,
        0,
        plain_text=f"{info['count']}",
        color=(255, 255, 255, 0),
        font_size=40,
        font_color=(211, 64, 33),
    )
    lik_text1_img = BuildImage(
        0, 0, plain_text="当前", color=(255, 255, 255, 0), font_size=20
    )
    lik_text2_img = BuildImage(
        0,
        0,
        plain_text=f"好感度：{impression:.2f}",
        color=(255, 255, 255, 0),
        font_size=30,
    )
    watermark = BuildImage(
        0,
        0,
        plain_text=f"{NICKNAME}@{pcr_now1.year}",
        color=(255, 255, 255, 0),
        font_size=15,
        font_color=(155, 155, 155),
    )
    today_data = BuildImage(300, 300, color=(255, 255, 255, 0), font_size=20)
    if is_sign:
        today_sign_text_img = BuildImage(
            0, 0, plain_text="", color=(255, 255, 255, 0), font_size=30
        )
        '''
        if impression_list:
            impression_list.sort(reverse=True)
            index = impression_list.index(impression)
            rank_img = BuildImage(
                0,
                0,
                plain_text=f"* 此群好感排名第 {index + 1} 位",
                color=(255, 255, 255, 0),
                font_size=30,
            )
            A.paste(rank_img, ((A.w - rank_img.w - 10), 20), True)
        '''
        today_data.text(
            (0, 0),#
            f"上次签到日期：{'从未'if not info['count'] else datetime.strptime(info['signtime'],'%Y-%m-%d %H:%M').date()}",
        )
        today_data.text((0, 25), f"总金币：{gold}")
        default_setu_prob = random.randint(1, 100)
        today_data.text(
            (0, 50),
            f"出金概率：{(default_setu_prob + impression if impression+default_setu_prob < 100 else 100):.2f}%",
        )
        today_data.text((0, 75), f"开箱次数：{(20 + int(impression / 3))}")
        _type = "view"
    else:
        A.paste(gift_border, (570, 140), True)
        today_sign_text_img = BuildImage(
            0, 0, plain_text="今日签到", color=(255, 255, 255, 0), font_size=30
        )
        if 0:#is_double:
            today_data.text((0, 0), f"好感度 + {impression_added / 2:.2f} × 2")
        else:
            today_data.text((0, 0), f"好感度 + {impression_added:.2f}")
        today_data.text((0, 25), f"金币 + {gold_add}")
        _type = "sign"
    #current_date = datetime.now()
    week = pcr_now1.isoweekday()
    data = pcr_now1.date()
    hour = pcr_now1.hour
    minute = pcr_now1.minute
    second = pcr_now1.second
    data_img = BuildImage(
        0,
        0,
        plain_text=f"时间：{data} {weekdays[week]} {hour}:{minute}:{second}",
        color=(255, 255, 255, 0),
        font_size=20,
    )
    info['gold']=gold
    info['impression']=impression
    info['signtime']=pcr_now
    
    abc[qid]=info
    with open(DATA_PATH/dataname,'w',encoding='utf-8') as f:
        json.dump(abc,f,ensure_ascii=False,indent=3)
        f.close()
    bk.paste(nickname_img, (30, 15), True)
    bk.paste(uid_img, (30, 85), True)
    bk.paste(A, (0, 150), alpha=True)
    bk.text((30, 167), "Accumulative check-in for")
    _x = bk.getsize("Accumulative check-in for")[0] + sign_day_img.w + 45
    bk.paste(sign_day_img, (346, 158), True)
    bk.text((_x, 167), "days")
    bk.paste(data_img, (220, 370), True)
    bk.paste(lik_text1_img, (220, 240), True)
    bk.paste(lik_text2_img, (262, 234), True)
    bk.paste(bar_bk, (225, 275), True)
    bk.paste(info_img, (220, 305), True)
    bk.paste(today_sign_text_img, (550, 180), True)
    bk.paste(today_data, (580, 220), True)
    bk.paste(watermark, (15, 400), True)#_{user.group_id}_{_type}_{data}
    bk.save(
        SAVE_PATH/f"{qid}.png"
    )
    return
#name='abc'
#qid=123
dataname="sign.json"
info=dict()
pcr_now = datetime.now()
pcr_now1 = datetime.now(tz)
pcr_now1+= timedelta(hours=8)
pcr_now=pcr_now1.strftime(r"%Y-%m-%d %H:%M")
if not os.path.exists(DATA_PATH/dataname):
    abc=open(DATA_PATH/dataname,'w',encoding='utf-8')
    abc.close()
    abc=dict()
elif os.path.getsize(DATA_PATH/dataname)>0:
    with open(DATA_PATH/dataname,'r',encoding='utf-8')as f:
        abc=json.load(f)
        f.close()
    if str(qid) in abc:
        info=abc[str(qid)]
        #gold=abc['gold']
        #impression=abc['impression']
        #signtime=abc['sign']
else:
    abc=dict()

if not info:
    info['gold']=0
    info['impression']=0
    info['signtime']=pcr_now
    info['count']=0
    is_sign=False
else:
    date1=datetime.strptime(pcr_now,"%Y-%m-%d %H:%M").date()
    date2=datetime.strptime(info['signtime'],"%Y-%m-%d %H:%M").date()
    if date1>date2: 
        is_sign=False
    else:
        is_sign=True
#print(date1,date2)
#gold=get_gold(qid)
get_card(name)
