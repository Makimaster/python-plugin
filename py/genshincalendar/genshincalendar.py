# -*- coding: utf-8 -*-
import base64
from .generate import *
from io import BytesIO
import os
import re
import traceback
HELP_STR = '''
原神活动日历
原神日历 : 查看本群订阅服务器日历
原神日历 on/off : 订阅/取消订阅指定服务器的日历推送
原神日历 time 时:分 : 设置日历推送时间
原神日历 status : 查看本群日历推送设置
'''.strip()

group_data = {}
def load_data():
    path = os.path.join(os.path.dirname(__file__), 'data.json')
    if not os.path.exists(path):
        return
    try:
        with open(path, encoding='utf8') as f:
            data = json.load(f)
            for k, v in data.items():
                group_data[k] = v
    except:
        traceback.print_exc()


def save_data():
    path = os.path.join(os.path.dirname(__file__), 'data.json')
    try:
        with open(path, 'w', encoding='utf8') as f:
            json.dump(group_data, f, ensure_ascii=False, indent=2)
    except:
        traceback.print_exc()
        
def update_group_schedule(group_id):
    group_id = str(group_id)
    if group_id not in group_data:
        return
    nonebot.scheduler.add_job(
        send_calendar,
        'cron',
        args=(group_id,),
        id=f'genshin_calendar_{group_id}',
        replace_existing=True,
        hour=group_data[group_id]['hour'],
        minute=group_data[group_id]['minute']
    )

def calendar():
    server = 'cn'
    im =generate_day_schedule(server)
    #im.save(os.path.dirname(__file__)+'/日历.png')
    return im
    #im.save(os.path.dirname(__file__)+'/日历.png')
    #base64_str = im2base64str(im)
