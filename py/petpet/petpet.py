#!--utf-8--
import sys
from functions import *
from download import get_head,download_url,get_name
from utils import to_image,to_image1,help_image
from io import BytesIO
from PIL import Image
from gif_subtitle_memes import *
import imghdr
from models import UserInfo, Command

commands = [
    Command(("鲁迅说", "鲁迅说过"),luxunsay),
    Command(("摸", "摸摸", "摸头", "摸摸头", "rua"), petpet, arg_num=1),
    Command(("亲", "亲亲"), kiss),
    Command(("贴", "贴贴", "蹭", "蹭蹭"), rub),
    Command(("顶", "玩"), play),
    Command(("拍",), pat),
    Command(("撕",), rip, arg_num=2),
    Command(("丢", "扔"), throw),
    Command(("抛", "掷"), throw_gif),
    Command(("爬","给爷爬"), crawl, arg_num=1),
    Command(("精神支柱",), support),
    Command(("一直",), always, convert=False),
    Command(("加载中",), loading, convert=False),
    Command(("转",), turn),
    Command(("小天使",), littleangel, convert=False, arg_num=1),
    Command(("不要靠近",), dont_touch),
    Command(("一样",), alike),
    Command(("滚",), roll),
    Command(("玩游戏", "来玩游戏"), play_game, convert=False, arg_num=1),
    Command(("膜", "膜拜"), worship),
    Command(("吃",), eat),
    Command(("可达鸭",), psyduck),
    Command(("啃",), bite),
    Command(("出警",), police),
    Command(("警察",), police1, convert=False),
    Command(("问问", "去问问"), ask, convert=False, arg_num=1),
    Command(("舔", "舔屏", "prpr"), prpr, convert=False),
    Command(("搓",), twist),
    Command(("墙纸",), wallpaper, convert=False),
    Command(("国旗",), china_flag),
    Command(("交个朋友",), make_friend, convert=False, arg_num=1),
    Command(("继续干活",), back_to_work, convert=False),
    Command(("完美", "完美的"), perfect, convert=False),
    Command(("关注",), follow, arg_num=1),
    Command(("我朋友说", "我有个朋友说"), my_friend, arg_num=10),
    Command(("这像画吗",), paint, convert=False),
    Command(("震惊",), shock),
    Command(("喜报",),goodnews),
    Command(("兑换券",), coupon, arg_num=2),
    Command(("听音乐",), listen_music),
    Command(("典中典",), dianzhongdian, convert=False, arg_num=3),
    Command(("哈哈镜",), funny_mirror),
    Command(("永远爱你",), love_you),
    Command(("对称",), symmetric, convert=False, arg_num=1),
    Command(("安全感",), safe_sense, convert=False, arg_num=2),
    Command(("永远喜欢", "我永远喜欢"), always_like, convert=False, arg_num=10),
    Command(("采访",), interview, arg_num=1),
    Command(("打拳",), punch, convert=False),
    Command(("群青",), cyan),
    Command(("捣",), pound),
    Command(("捶",), thump),
    Command(("需要", "你可能需要"), need),
    Command(("捂脸",), cover_face),
    Command(("结婚申请", "结婚登记"),marriage),
    Command(("阿尼亚喜欢","阿妮亚喜欢"),anyasuki),
    Command(("敲",), knock),
    Command(("垃圾", "垃圾桶"), garbage),
    Command(("为什么@我", "为什么at我"), whyatme),
    Command(("像样的亲亲",), decent_kiss, convert=False),
    Command(("小画家",),painter, ),
    Command(("你好骚啊",),nihaosaoa,typing='gif'),
    Command(("王境泽",),wangjingze,typing='gif'),
    Command( ("为所欲为",),weisuoyuwei,typing='gif'),
    Command( ("馋身子",),chanshenzi,typing='gif'),
    Command(("切格瓦拉",),qiegewala,typing='gif' ),
    Command(("谁反对",),shuifandui,typing='gif' ),
    Command(("曾小贤",),zengxiaoxian,typing='gif' ),
    Command( ("压力大爷",),yalidaye,typing='gif'),
    Command(("五年怎么过的",),wunian,typing='gif' ),
]

userid=sys.argv[1]
if userid=='help':
    help_image(commands)
    exit()


target=sys.argv[2]
key=sys.argv[3]
keys=key.split("_")
sex=sys.argv[4]
image1=get_head(userid)
image1=to_image(image1)
text=''
if 'http' in target:
    image2=download_url(target)  
    image2=to_image2(image2)
    if '，' in sex:
        names=sex.split('，')
        name=names[0]
        if not names[1]:
            sex='male'
        else:
            sex=names[1]
    else:
        name=''
else:
    image2=get_head(target)
    image2=to_image(image2)
    name=get_name(target)


for abc in commands:
    for i in abc.keywords:
        if i == keys[0]:
            abd=abc.func
            a=len(keys[0])
            if not text:
                text=key[a:].replace('_','')
            if abc.typing=='gif':
                abd()
                break
            
            abd(image2,image1,text,name,sex)
            break



