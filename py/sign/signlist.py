import json
import sys,os
from pathlib import Path
import matplotlib.pyplot as plt
FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../../resrouces")
SIGN_RESOURCE_PATH = Path(__file__).parent.parent.parent / "resrouces" / "sign_res"
SAVE_PATH=Path(__file__).parent.parent.parent / "resrouces" / 'today_card'
DATA_PATH=Path(__file__).parent.parent.parent/"data"
dataname="sign.json"
if not os.path.exists(DATA_PATH/dataname):
    abc=open(DATA_PATH/dataname,'w',encoding='utf-8')
    abc.close()
elif os.path.getsize(DATA_PATH/dataname)>0:
    with open(DATA_PATH/dataname,'r',encoding='utf-8')as f:
        abc=json.load(f)
        f.close()    
    x=[]
    y=[]
    n=0
    for i in abc:
        x.append(i)
        y.append(abc[i]['impression'])
        n+=1
    plt.bar(x,y)
    plt.savefig(SAVE_PATH/"1.png")
    exit()
print('error')
    

