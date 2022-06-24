import requests
import json

url='https://api-static.mihoyo.com/common/blackboard/ys_obc/v1/get_red_point_info?app_sn=ys_obc'
res=requests.get(url).json()
print(res)
'''
with open('124.json','w') as g:
    a=json.dumps(res,indent=3)
    g.write(a)

with open('123.json','r')as f:
    a=json.load(f)
    f.close()

b=a['data']['posts']
for i in b:
    a=i['post']['structured_content'].replace('{',"'{").replace('}',"}'")
    print(a[0:20])
    for j in a:
        print(j)
        exit()
    for j in list(i['post']['structured_content']):
        print(j)
        if '早柚' in j:
            print(j)
        
          
c=requests.get(url).content
with open('123.png','wb')as f:
    f.write(c)
'''

