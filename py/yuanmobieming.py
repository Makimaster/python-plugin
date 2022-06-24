import json
import os,sys

FILE_PATH1 = os.path.dirname(__file__)
DATA_PATH=os.path.join(FILE_PATH1,"../data")
if not os.path.exists(DATA_PATH+'/enemies_name.json'):    
    with open(DATA_PATH+'/enemies.json','r',encoding="UTF-8") as f:
        im1=json.load(f)
        f.close()
    name=dict()
    with open(DATA_PATH+'/enemies_name.json','w',encoding="UTF-8") as f:
        for i in im1:
            name[i]=[]
        json.dump(name,f,ensure_ascii=False,indent=1)
        f.close()

with open(DATA_PATH+'/enemies_name.json','r',encoding="UTF-8") as f:
    im1=json.load(f)
    f.close()

name=sys.argv[1]
name2=sys.argv[2]
for i in im1:
    if name in i or name in im1[i]:
        if name2 in im1[i] or  name == i:
            print('error2')
            exit()
        else:
            im1[i].append(name2)
            with open(DATA_PATH+'/enemies_name.json','w',encoding="UTF-8") as f:
                json.dump(im1,f,ensure_ascii=False,indent=1)
                f.close()
                exit()

print('error1')
