
import hashlib
import requests
import os
import json

FILE_PATH1 = os.path.dirname(__file__)
data_path = os.path.join(FILE_PATH1,"../../resrouces")


class DownloadError(Exception):
    pass


class ResourceError(Exception):
    pass


def download_url(url: str) -> bytes:
    resp=requests.get(url).content
    
    return resp


def get_resource(path: str, name: str) -> bytes:
    file_path = data_path +'/'+ path+'/'+ name
    if not os.path.exists(file_path):
        #file_path.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://cdn.jsdelivr.net/gh/MeetWq/nonebot-plugin-petpet@master/resources/{path}/{name}"
        data = download_url(url)
        if data:
            with open(str(file_path), "wb") as f:
                f.write(data)
    if not os.path.exists(file_path):
        raise ResourceError
    with open(str(file_path), "rb") as f:
        return f.read()
def get_head(user_id):
    url=f'http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=640'
    return download_url(url)


def get_image(name: str) -> bytes:
    return get_resource("images", name)

def get_name(user_id):
    url=f'http://api.usuuu.com/qq/{user_id}'
    resp=requests.get(url).json()['data']['name']
    return resp


def get_font(name: str) -> bytes:
    return get_resource("fonts", name)



def download_avatar(user_id: str) -> bytes:
    url = f"http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=640"
    data = download_url(url)
    if not data or hashlib.md5(data).hexdigest() == "acef72340ac0e914090bd35799f5594e":
        url = f"http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=100"
        data = download_url(url)
        if not data:
            raise DownloadError
    return data
