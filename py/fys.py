# -*- coding: utf-8 -*-
import sys,json,os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import time

FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../resrouces")
DATA_PATH=os.path.join(FILE_PATH1,"../data")
FONT_PATH = os.path.join(FILE_PATH, "fonts", "hanyiheiti.ttf")
SUICAI_PATH=os.path.join(FILE_PATH,"suicai")
ROUSE_PATH="./resources/genshin/logo/reliquaries/"
ENEMIES_PATH=os.path.join(FILE_PATH,'enemies_head')
url='https://genshin.honeyhunterworld.com'
tubiao=dict()
tubiao['def_def']='/img/icons/buffs/def_def_35.png'#物抗
tubiao['pyro']='/img/icons/element/pyro_35.png'#火抗
tubiao['dendro']='/img/icons/element/dendro_35.png'#草抗
tubiao['hydro']='/img/icons/element/hydro_35.png'#水抗
tubiao['electro']='/img/icons/element/electro_35.png'#雷抗
tubiao['anemo']='/img/icons/element/anemo_35.png'#风抗
tubiao['cryo']='/img/icons/element/cryo_35.png'#冰抗
tubiao['geo']='/img/icons/element/geo_35.png'#岩抗
        

if not os.path.exists(FONT_PATH):
    FONT_PATH = os.path.join(FILE_PATH, "fonts", "汉仪黑体.ttf")
lot_font = ImageFont.truetype(FONT_PATH, 25)
title_font = ImageFont.truetype(FONT_PATH, 40)
artifacts_im = '''【{}】
【稀有度】：{}
【2件套】：{}
【4件套】：{}
【{}】：{}
【{}】：{}
【{}】：{}
【{}】：{}
【{}】：{}
'''
food_im = '''【{}】
【稀有度】：{}
【食物类型】：{}
【食物类别】：{}
【效果】：{}
【介绍】：{}
【材料】：{}
'''
def foods_wiki(name):
    data =get_misc_info("foods", name)
    if "errcode" in data:
        im = "该食物不存在。"
        return im,0
    else:
        ingredients = ""
        food_temp = {}
        for i in data["ingredients"]:
            if i["name"] not in food_temp:
                food_temp[i["name"]] = i["count"]
            else:
                food_temp[i["name"]] = food_temp[i["name"]] + i["count"]
        for i in food_temp:
            ingredients += i + ":" + str(food_temp[i]) + "\n"
        ingredients = ingredients[:-1]
        im = food_im.format(data["name"], data["rarity"], data["foodtype"], data["foodfilter"], data["effect"],
                            data["description"], ingredients)
        return im,1

def get_misc_info(mode, name):
    url = "https://info.minigg.cn/{}".format(mode)
    req=requests.get(
            url=url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/97.0.4692.71 Safari/537.36'},
            params={"query": name}
        )
    
    data = json.loads(req.text)
    return data


def artifacts_wiki(name):
    data =get_misc_info("artifacts", name)
    if "errcode" in data:
        im = "该圣遗物不存在。"
        return im,0
    else:
        star = ""
        for i in data["rarity"]:
            star = star + i + "星、"
        star = star[:-1]
        im = artifacts_im.format(data["name"], star, data["2pc"], data["4pc"], data["flower"]["name"],
                                 data["flower"]["description"],
                                 data["plume"]["name"], data["plume"]["description"], data["sands"]["name"],
                                 data["sands"]["description"],
                                 data["goblet"]["name"], data["goblet"]["description"], data["circlet"]["name"],
                                 data["circlet"]["description"])
        #name=[]
        #name=name+data["name"]+data["flower"]["name"]+data["plume"]["name"]+data["sands"]["name"]+data["goblet"]["name"]+data["circlet"]["name"]
        return im,data
    




def draw_pic(im,model,name,filename):
    #im=artifacts_wiki(name)
       
    if model=='artifacts':
        text=''
        bg = Image.new("RGB",(800,3000),(255,255,255))
        pen = ImageDraw.Draw(bg)
        y=150
        x=50
        char_img = Image.open(ROUSE_PATH+name["flower"]["name"]+'.png').resize((100, 100))
        bg.paste(char_img, (50, 50),char_img)
        char_img = Image.open(ROUSE_PATH+name["plume"]["name"]+'.png').resize((100, 100))
        bg.paste(char_img, (175, 50),char_img)
        char_img = Image.open(ROUSE_PATH+name["sands"]["name"]+'.png').resize((100, 100))
        bg.paste(char_img, (300, 50),char_img)
        char_img = Image.open(ROUSE_PATH+name["goblet"]["name"]+'.png').resize((100, 100))
        bg.paste(char_img, (425, 50),char_img)
        char_img = Image.open(ROUSE_PATH+name["circlet"]["name"]+'.png').resize((100, 100))
        bg.paste(char_img, (550, 50),char_img)
        for i in im:
            if i=='\n':
                pen.text((x, y), text, fill="#8d7650ff", font=lot_font)
                text=''
                y=y+lot_font.size*1.5
            else:
                text=text+i
                if len(text)>=25:
                    pen.text((x, y), text, fill="#8d7650ff", font=lot_font)
                    text=''
                    y=y+lot_font.size*1.5
        bg1=bg.crop((0,0,700,int(y+lot_font.size*1.5)))
    elif model=='food':
        text=''
        bg = Image.new("RGB",(800,3000),(255,255,255))
        pen = ImageDraw.Draw(bg)
        y=50
        x=50
        for i in im:
            if i=='\n':
                pen.text((x, y), text, fill="#8d7650ff", font=lot_font)
                text=''
                y=y+lot_font.size*1.5
            else:
                text=text+i
                if len(text)>=25:
                    pen.text((x, y), text, fill="#8d7650ff", font=lot_font)
                    text=''
                    y=y+lot_font.size*1.5
        bg1=bg.crop((0,0,700,int(y+lot_font.size*1.5)))
    elif model=='enemies_info':
        bg = Image.new("RGB",(1800,3000),(255,255,255))
        pen = ImageDraw.Draw(bg)
        y=50
        x=50
        dx=len(im)-23
        tx=445-int(len(name)/2)*title_font.size
        y=330
        char_img=Image.open(ENEMIES_PATH+'/'+name+'.png').resize((100,100))
        bg.paste(char_img, (50, 50),char_img)
        pen.text((tx, 50), name, fill="#8d7650ff", font=title_font)
        n=0
        drop_x=200
        drop_y=100
        #绘制掉落物品
        for i in list(im)[:dx]:          
            #物品图片
            if  not os.path.exists(SUICAI_PATH+'/'+i+'.png'):
                url1=url+im[i][0]
                res1=requests.get(url1).content
                avatar1=Image.open(BytesIO(res1)).resize((50,50))
                avatar1.save(SUICAI_PATH+'/'+i+'.png')
                time.sleep(3)
            else:
                avatar1 = Image.open(SUICAI_PATH+'/'+i+'.png').resize((50,50))
            #背景图片
            if  not os.path.exists(SUICAI_PATH+'/'+im[i][1].replace('/img/back/item/','')):
                
                url2=url+im[i][1]
                res2=requests.get(url2).content
                avatar2=Image.open(BytesIO(res2)).resize((50,50))
                avatar2.save(SUICAI_PATH+'/'+im[i][1].replace('/img/back/item/',''))
            else:
                avatar2 = Image.open(SUICAI_PATH+'/'+im[i][1].replace('/img/back/item/','')).resize((50,50))
            avatar2.paste(avatar1,(0,0),avatar1)
            bg.paste(avatar2,(drop_x,drop_y))
            n=n+1
            drop_x=drop_x+55
            if n>=16:
                n=0
                drop_y=drop_y+55
                drop_x=200
        #绘制文字
        for i in list(im)[dx:-1]:
            pen.text((x, y), i, fill="#8d7650ff", font=lot_font)
            
            for j in im[i]:
                x=x+130
                pen.text((x, y), j, fill="#8d7650ff", font=lot_font)
            
            x=50
            y=y+lot_font.size*1.5
        #绘制抗性
        #贴图
        x=1100
        y1=100
        for i in tubiao:
            if not os.path.exists(SUICAI_PATH+'/'+i+'.png'):
                url3=url+tubiao[i]
                res3=requests.get(url3).content
                avatar3=Image.open(BytesIO(res3)).resize((50,50))
                avatar3.save(SUICAI_PATH+'/'+i+'.png')
            else:
                avatar3 = Image.open(SUICAI_PATH+'/'+i+'.png').resize((50,50))
            bg.paste(avatar3,(x,y1),avatar3)
            x=x+100
                
        x=1100    
        y1=170
        #文字
        for i in list(im)[-1:]:
            for j in im[i][3:]:
                pen.text((x, y1), j, fill="#8d7650ff", font=lot_font)
                
                x=x+100
            y1=y1+55
        bg1=bg.crop((0,0,1800,int(y+lot_font.size*1.5)))
        

    
    bg1.save(FILE_PATH+'/'+model+'/'+filename+".png")





if __name__=="__main__":
    command=sys.argv[1]
    
    if command[:2]=='食物':
        if not os.path.exists(FILE_PATH+'/food'):
            os.makedirs(FILE_PATH+'/food')
        if not os.path.exists(FILE_PATH+'/food/'+command[2:]+'.png'):
            im,name=foods_wiki(command[2:])
            if name==0:
                print('error')
                exit()
            draw_pic(im,'food',0,command[2:])
    elif command[:3]=='圣遗物':
        if not os.path.exists(FILE_PATH+'/artifacts'):
            os.makedirs(pILE_PATH+'/artifacts')
        if not os.path.exists(FILE_PATH+'/artifacts/'+command[3:]+'.png'):
            im,name=artifacts_wiki(command[3:])
            if name==0:
                print('error')
                exit()
            draw_pic(im,'artifacts',name,command[3:])   
    else:
        if not os.path.exists(FILE_PATH+'/enemies_info'):
            os.makedirs(FILE_PATH+'/enemies_info')
        if not os.path.exists(FILE_PATH+'/enemies_info/'+command[2:]+'.png'):
            im=get_misc_info("enemies", command[2:])
            if "errcode" in im:
                print('error')
                exit()
            name =im['name']                                    
            with open(DATA_PATH+'/enemies.json','r',encoding="UTF-8") as f:
                im=json.load(f)
                f.close()
            
            draw_pic(im[name],'enemies_info',name,command[2:])
        
        
        
