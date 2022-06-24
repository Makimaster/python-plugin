import re
import random
import itertools
import traceback
from typing import List, Tuple, Optional

import sys,json,os
from life import Life
from talent import Talent
from PicClass import *

FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../../resrouces")
DATA_PATH=os.path.join(FILE_PATH1,'../../data/data')

def start():
    life_ = Life()
    life_.load()
    state=dict()
    #print()
    talents = life_.rand_talents(10)
    state["life"] = life_
    state["talents"] = talents
    msg = "请发送编号选择3个天赋，如“选择0,1,2”，或发送“随机”随机选择\n"
    des = msg+"\n".join([f"{i}.{t}" for i, t in enumerate(talents)])
    talent=[t.id for i,t in enumerate(talents)]
    a=dict()
    #print(talent,des)
    a[qid]=talent
    with open(DATA_PATH+'/user.json','w')as f:
        a=json.dumps(a)
        f.write(a)
        f.close()
    img=ImgText(des).draw_text()
    if not os.path.exists(FILE_PATH+'/life1'):
        os.makedirs(FILE_PATH+'/life1')
    img.save(FILE_PATH+'/life1/'+qid+'.png')


def talent(talents,reply):

    life_ = Life()
    #talents: List[Talent] #= state["talents"]

    match = re.findall(r"\d+", reply)
    if match:
        nums = [int(n) for n in match]
        nums.sort()
        if nums[-1] >= 10:
            print("error")

        talents_selected = [talents[n] for n in nums]
    elif reply == "随机":
        while True:
            nums = random.sample(range(10), 3)
            nums.sort()
            talents_selected = [talents[n] for n in nums]

    else:
        print("error")

    #life_.set_talents(talents_selected)
    #state["talents_selected"] = talents_selected

    msg = (
        "请发送4个数字分配“颜值、智力、体质、家境”4个属性，如“分配5.5.5.5”，或发送“随机”随机选择；"
        f"可用属性点为{life_.total_property()}，每个属性不能超过10"
    )
    a=dict()
    a[qid]=talents_selected
    with open(DATA_PATH+'/user.json','w')as f:
        a=json.dumps(a)
        f.write(a)
        f.close()
    img=ImgText(msg).draw_text()
    img.save(FILE_PATH+'/life1/'+qid+'.png')



def game(state,reply):
    life_= Life()
    life_.load()
    a=[]
    #print(life_.talent.talent_dict)
    for i in life_.talent.talent_dict[0]:
        for j in state:
            if i.id==j:
                life_.set_talents([i])
                a.append(i)
    
    talents: List[Talent]=a
    total_prop = life_.total_property()
    
    match = re.findall(r"\d+", reply)
    if match:
        nums = [int(n) for n in match]
        if sum(nums) > total_prop:
            print("error")
        elif max(nums) > 10:
            print("error")

    elif reply == "随机":
        half_prop1 = int(total_prop / 2)
        half_prop2 = total_prop - half_prop1
        num1 = random.randint(0, half_prop1)
        num2 = random.randint(0, half_prop2)
        nums = [num1, num2, half_prop1 - num1, half_prop2 - num2]
        random.shuffle(nums)
    else:
        print("error")

    prop = {"CHR": nums[0], "INT": nums[1], "STR": nums[2], "MNY": nums[3]}
    life_.apply_property(prop)

    #print("你的人生正在重开...")

    msgs = [
        "你的人生正在重开...",
        "已选择以下天赋：\n" + "\n".join([str(t) for t in talents]),
        "已设置如下属性：\n" + f"颜值{nums[0]} 智力{nums[1]} 体质{nums[2]} 家境{nums[3]}",
    ]
    pic_list = []
    for i in msgs:
        pic_list.append(ImgText(i).draw_text())
    try:
        life_msgs = []
        for s in life_.run():
            life_msgs.append("\n".join(s))
        n = 5
        life_msgs = [
            "\n".join(life_msgs[i : i + n]) for i in range(0, len(life_msgs), n)
        ]
        #msgs.extend(life_msgs)
        for i in life_msgs:
            pic_list.append(ImgText(i).draw_text())
        pic_list.append(ImgText(life_.gen_summary()+'/n').draw_text())
        #msgs.append(life_.gen_summary())
        draw_pic(pic_list,qid)
    except Exception as e:
        print("error",e)
name=sys.argv[1]
qid=sys.argv[2]
command=sys.argv[3]
args=sys.argv[4]
if command=='开始':
    start()
elif command=='天赋':
    with open(DATA_PATH+'/user.json','r')as f:
        a=json.load(f)
        #a=f.read()
        f.close()
    talent(a[qid],args)
elif command=='属性':
    with open(DATA_PATH+'/user.json','r')as f:
        a=json.load(f)
        f.close()
        game(a[qid],args)


