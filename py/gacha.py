import json
import sys,os
import xlrd
from pathlib import Path
qid=sys.argv[1]
uid=sys.argv[2]
FILE_PATH1 = os.path.dirname(__file__)
name=qid+'.xlsx'
DATA_PATH=Path(__file__).parent.parent.parent.parent /"data"/"file"/"output_log"/name
GACHA_PATH=Path(__file__).parent.parent.parent.parent /"data"/'html'/'genshin'/'gachaJson'/qid/uid

if not os.path.exists(GACHA_PATH):
     os.makedirs(GACHA_PATH)
wb =xlrd.open_workbook(DATA_PATH)#换成你的表格
sh=wb.sheet_names()#获取所有表格
#第一个表格

for j in range(len(sh)):
     if '角色' in sh[j]:
          up_chi='301'
     elif '武器'in sh[j]:
          up_chi='302'
     elif '常驻' in sh[j]:
          up_chi='200'
     else:
          continue
     ws=wb.sheet_by_name(sh[j])#第几个表格
     b=dict() 
     for i in range(1,ws.nrows):
          a=dict()
          a['uid']=uid
          a['gacha_type']=up_chi
          a['item_id']=''
          a['count']='1'
          a['time']=ws.row_values(i)[0]
          a['name']=ws.row_values(i)[1]
          a['lang']='zh-cn'
          a['item_type']=ws.row_values(i)[2]
          a['rank_type']=ws.row_values(i)[3]
          a['id']=ws.row_values(i)[6]
          b[ws.row_values(i)[6]]=a
     
     name1=up_chi+'.json'
     if not os.path.exists(GACHA_PATH/name1):
          abc=open(GACHA_PATH/name1,'w',encoding='utf-8')
          abc.close()
     elif os.path.getsize(GACHA_PATH/name1)>0:          
          with open(GACHA_PATH/name1,'r',encoding='utf-8')as f:
               abc=json.load(f)
               f.close()
          for k in abc:
               b[k['id']]=k
     c=[]
     for i in b:
          c.append(b[i])
     
     c.sort(key=lambda x:x['id'],reverse=True)
     with open(GACHA_PATH/name1,'w',encoding='utf-8')as f:
          f.seek(0)
          f.truncate()
          a=json.dumps(c,ensure_ascii=False)
          f.write(a)
          f.close()

os.remove(DATA_PATH)
