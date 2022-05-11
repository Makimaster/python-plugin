# -*- coding: utf-8 -*-
import os
import json
FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../resrouces")
if not os.path.exists(FILE_PATH+'/qianwen'):
    os.makedirs(FILE_PATH+'/qianwen')
if not os.path.exists(FILE_PATH+'/jieqian'):
    os.makedirs(FILE_PATH+'/jieqian')
if not os.path.exists(FILE_PATH+'/enemies_info'):
    os.makedirs(FILE_PATH+'/enemies_info')

path=os.listdir(FILE_PATH+'/qianwen')
for i in path:
    os.remove(FILE_PATH+'/qianwen/'+i)


path1=os.listdir(FILE_PATH+'/enemies_info')
for j in path1:
    #清理绘制好的原魔信息
    os.remove(FILE_PATH+'/enemies_info/'+j)


path2=os.listdir(FILE_PATH+'/qianwen')
for k in path2:
    os.remove(FILE_PATH+'/qianwen/'+k)
a=dict()
DATA_PATH=os.path.join(FILE_PATH1,"../data")
with open(DATA_PATH+'/config.json','w') as g:
    a=json.dumps(a)
    g.write(a)
