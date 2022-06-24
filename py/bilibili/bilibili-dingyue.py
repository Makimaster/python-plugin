import requests
import time,json
import os,sys
from hashlib import md5
from urllib.parse import urlencode
from typing import Any, Dict, Optional
DEFAULT_HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
        "Safari/537.36 Edg/87.0.664.60"
    ),
    "Referer": "https://www.bilibili.com/",
}
uid=sys.argv[2]
APPSEC = "59b43e04ad6965f34319062b478f83dd"
APPKEY = "4409e2ce8ffd12b8"
model=sys.argv[3]
gid=sys.argv[1]
FILE_PATH1 = os.path.dirname(__file__)
DATA_PATH=os.path.join(FILE_PATH1,"../../data")
#用户信息api
url_n='https://api.bilibili.com/x/space/acc/info'
params_n = {"mid": uid}
#用户视频历史
url_d='https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history'
params_d = {
    "host_uid": uid,
    "offset_dynamic_id": 0,
    "need_top": int(bool(False)),
    }
#用户动态历史
url_v = f"https://api.bilibili.com/x/space/arc/search"
params_v = {
    "mid": uid,
    "ps": 30,
    "tid": 0,
    "pn": 1,
    "keyword": "",
    "order": "pubdate"
    }
url_m = f"https://api.bilibili.com/pgc/review/user"
params_m = {"media_id": uid}

url_l='https://api.live.bilibili.com/room/v1/Room/get_info'
params_l = {"id": uid}

def _encrypt_params(params: Dict[str, Any], local_id: int = 0) -> Dict[str, Any]:
    params["local_id"] = local_id
    params["appkey"] = APPKEY
    params["ts"] = int(time.time())
    params["sign"] = md5(
        f"{urlencode(sorted(params.items()))}{APPSEC}".encode("utf-8")
    ).hexdigest()
    return params

def request(
    url,
    params,
    model=model,
    headers=DEFAULT_HEADERS,
):
    _encrypt_params(params)
    
    resp = requests.get(
        url=url, headers=headers, params=params
        )
    resp.encoding = "utf-8"
    
    if resp.json()["code"] != 0:
        print('requesterror')
        exit()
    if model =='番剧':
        return resp.json()["result"]
    return resp.json()["data"]

    


if model=='up':
    #查询用户信息    
    resq=request(url_n,params_n)
    uname=resq["name"]    
    dynamic=request(url_d,params_d)
    if dynamic.get("cards"):
        dynamic = dynamic["cards"][0]["desc"]["timestamp"]    
    video=request(url_v,params_v)
    if video["list"].get("vlist"):
        video = video["list"]["vlist"][0]["created"]
    name1='/bilibili.json'
    b=dict()
    if not os.path.exists(DATA_PATH+name1):
        abc=open(DATA_PATH+name1,'w',encoding='utf-8')
        a=json.dumps(b,ensure_ascii=False)
        abc.write(a)
        abc.close()
    with open(DATA_PATH+name1,'r',encoding='utf-8') as f:
        b=json.load(f)
        f.close()
    if len(b)>0:
        for i in b:
            if str(b[i]['uid'])==str(uid) and str(b[i]['gid'])==str(gid):
                print('already')
                exit()
    a=dict()
    a['type']='up'
    a['uname']=uname
    a['uid']=uid
    a['gid']=gid
    a['dynamic']=dynamic
    a['video']=video
    b[str(gid)+str(uid)]=a
    #写入json
    with open(DATA_PATH+name1,'w',encoding='utf-8')as f:
        a=json.dumps(b,ensure_ascii=False,indent=1)
        f.write(a)
        f.close()
    print(str(gid)+str(uid))
elif model=='删除':
    name1='/bilibili.json'
    b=dict()
    if not os.path.exists(DATA_PATH+name1):
        abc=open(DATA_PATH+name1,'w',encoding='utf-8')
        a=json.dumps(b,ensure_ascii=False)
        abc.write(a)
        abc.close()
    with open(DATA_PATH+name1,'r',encoding='utf-8') as f:
        b=json.load(f)
        f.close()
    if len(b)>0:
        for i in b:
            if str(b[i]['uid'])==str(uid) and str(b[i]['gid'])==str(gid):
                del b[i]
                
                with open(DATA_PATH+name1,'w',encoding='utf-8')as f:
                    a=json.dumps(b,ensure_ascii=False,indent=1)
                    f.write(a)
                    f.close()
                print('success')
                exit()
    
    print('empty')
elif model=='番剧':
    resq=request(url_m,params_m)
    uid = resq["media"]["season_id"]
    season_current_episode = resq["media"]["new_ep"]["index"]
    season_name = resq["media"]["title"]
    name1='/bilibili.json'
    b=dict()
    if not os.path.exists(DATA_PATH+name1):
        abc=open(DATA_PATH+name1,'w',encoding='utf-8')
        a=json.dumps(b,ensure_ascii=False)
        abc.write(a)
        abc.close()
    with open(DATA_PATH+name1,'r',encoding='utf-8') as f:
        b=json.load(f)
        f.close()
    a=dict()
    a['uid']=uid
    a['time']=season_current_episode
    a['uname']=season_name
    a['type']='media'
    a['gid']=gid
    b[str(gid)+str(uid)]=a
    with open(DATA_PATH+name1,'w',encoding='utf-8')as f:
        a=json.dumps(b,ensure_ascii=False,indent=1)
        f.write(a)
        f.close()
    print(str(gid)+str(uid))
elif model=='直播':
    resq=request(url_l,params_l)
    uid = resq["room_id"]
    short_id = resq["short_id"]
    title = resq["title"]
    live_status = resq["live_status"]
    name1='/bilibili.json'
    b=dict()
    if not os.path.exists(DATA_PATH+name1):
        abc=open(DATA_PATH+name1,'w',encoding='utf-8')
        a=json.dumps(b,ensure_ascii=False)
        abc.write(a)
        abc.close()
    with open(DATA_PATH+name1,'r',encoding='utf-8') as f:
        b=json.load(f)
        f.close()
    a=dict()
    a['uid']=uid
    a['uname']=title
    a['time']=live_status
    a['type']='live'
    a['gid']=gid
    b[str(gid)+str(uid)]=a
    with open(DATA_PATH+name1,'w',encoding='utf-8')as f:
        a=json.dumps(b,ensure_ascii=False,indent=1)
        f.write(a)
        f.close()
    print(str(gid)+str(uid))
