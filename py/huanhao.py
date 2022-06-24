import os,re
import json
FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH2=os.path.join(FILE_PATH1,"../Backcount")
FILE_PATH =os.path.join(FILE_PATH1,"../../../config")
if not os.path.exists(FILE_PATH2):
    os.makedirs(FILE_PATH2)
path=os.listdir(FILE_PATH2)
with open(FILE_PATH+'/config.js','r',encoding='utf-8')as f:
    a=f.read()
    f.close()
n=1
#将冻结账号配置拷贝到Backcount目录下
while n:
    if 'config-冻结'+str(n)+'.js' in path:
        n=n+1
        continue
    with open(FILE_PATH2+'/config-冻结'+str(n)+'.js','w',encoding='utf-8')as f:
        f.write(a)
        f.close()
        break

qq=re.findall('qq:"(.*?)",',a)
pwd=re.findall('pwd:"(.*?)",',a)
#移除已经冻结账号的配置，防止以后切换为该账号
for i in path:
    
    if i[-2:]=='js':
        with open(FILE_PATH2+'/'+i,'r',encoding='utf-8')as f:
            b=f.read()
            f.close()
        qq1=re.findall('qq:"(.*?)",',b)
        if qq1[0]==qq[0]:
            os.remove(FILE_PATH2+'/'+i)
            continue
path=os.listdir(FILE_PATH2)
#寻找可以切换的账号
for i in path:    
    if i[-2:]=='js':        
        if '冻结' in i:
            continue
        with open(FILE_PATH2+'/'+i,'r',encoding='utf-8')as f:
            b=f.read()
            f.close()
        qq1=re.findall('qq:"(.*?)",',b)
        if qq1[0]==qq[0]:
            os.remove(FILE_PATH2+'/'+i)
            continue
        print(qq[0],qq1[0])
        pwd1=re.findall('pwd:"(.*?)",',b)
        a=a.replace(qq[0],qq1[0])
        a=a.replace(pwd[0],pwd1[0])
        break
with open(FILE_PATH+'/config.js','w',encoding='utf-8')as f:
    f.write(a)
    f.close()
