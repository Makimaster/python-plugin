import requests
import json
import os,sys
DEFAULT_HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
        "Safari/537.36 Edg/87.0.664.60"
    ),
    "Referer": "https://www.bilibili.com/",
}
keyword=sys.argv[1]
bilibili_search_url = "https://api.bilibili.com/x/web-interface/search/all/v2"
params = {"keyword": keyword}
def get_media_id():
    """
    获取番剧的 media_id
    :param keyword: 番剧名称
    """
    
    for _ in range(3):
        try:
            _season_data = {}
            response = requests.get(
                bilibili_search_url, params=params, timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                if data.get("data"):
                    for item in data["data"]["result"]:
                        if item["result_type"] == "media_bangumi":
                            idx = 0
                            for x in item["data"]:
                                _season_data[idx] = {
                                    "media_id": x["media_id"],
                                    "title": x["title"]
                                    .replace('<em class="keyword">', "")
                                    .replace("</em>", ""),
                                }
                                idx += 1
                            return _season_data
        except TimeoutError:
            pass
        return {}
FILE_PATH1 = os.path.dirname(__file__)
DATA_PATH=os.path.join(FILE_PATH1,"../../data")
a=get_media_id()
with open(DATA_PATH+'/soufan.json','w',encoding='utf-8')as f:
    a=json.dumps(a,ensure_ascii=False,indent=1)
    f.write(a)
    f.close()
