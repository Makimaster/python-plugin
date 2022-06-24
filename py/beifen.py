import os,re

FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH2=os.path.join(FILE_PATH1,"../Backoff")
FILE_PATH =os.path.join(FILE_PATH1,"../../..")
FILE_PATH3=os.path.join(FILE_PATH),'/config/genshin/_list.js')

model=sys.argv[1]
if model=='读':
    with open(FILE_PATH2+'/backoff.txt','r',encoding='utf-8')as f:
        while True:
            a=f.readline()
            if a:
                a=a.split('#')[0]
                if a:
                    a=a.replace('\n','')
                    with open(FILE_PATH+a,'r',encoding='utf-8')as g:
                        b=g.read()
                        g.close()
                    a=a.split('/')[-1]
                    with open(FILE_PATH2+'/'+a,'w',encoding='utf-8')as g:
                        g.write(b)
                        g.close()
            else:
                break
        f.close()
    with open(FILE_PATH3+'roleId.js','r',encoding='utf-8')as f:
        a=f.read()
        f.close()
    with open(FILE_PATH3+'roleId_list.js','w',encoding='utf-8')as f:
        f.write(b)
        f.close()

elif model=='写':
    with open(FILE_PATH2+'/backoff.txt','r',encoding='utf-8')as f:
        while True:
            a=f.readline()
            if a:
                a=a.split('#')[0]
                if a:
                    a=a.replace('\n','')
                    c=a.split('/')[-1]
                    with open(FILE_PATH2+'/'+c,'r',encoding='utf-8')as g:
                        b=g.read()
                        g.close()
                    with open(FILE_PATH+a,'w',encoding='utf-8')as g:
                        g.write(b)
                        g.close()
            else:
                break
        f.close()
