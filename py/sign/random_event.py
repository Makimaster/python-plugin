#from configs.config import Config
import random


PROB_DATA = None

plugin_configs = {
    "MAX_SIGN_GOLD": {"value": 200, "help": "签到好感度加成额外获得的最大金币数", "default_value": 200},
    "SIGN_CARD1_PROB": {"value": 0.2, "help": "签到好感度双倍加持卡Ⅰ掉落概率", "default_value": 0.2},
    "SIGN_CARD2_PROB": {
        "value": 0.09,
        "help": "签到好感度双倍加持卡Ⅱ掉落概率",
        "default_value": 0.09,
    },
    "SIGN_CARD3_PROB": {
        "value": 0.05,
        "help": "签到好感度双倍加持卡Ⅲ掉落概率",
        "default_value": 0.05,
    },
}

def random_event(impression: float) -> 'Union[str, int], str':
    """
    签到随机事件
    :param impression: 好感度
    :return: 额外奖励 和 类型
    """
    global PROB_DATA
    if not PROB_DATA:
        PROB_DATA =dict()
        PROB_DATA[plugin_configs["SIGN_CARD3_PROB"]['value']]='好感度双倍加持卡Ⅲ'
        PROB_DATA[plugin_configs["SIGN_CARD2_PROB"]['value']]='好感度双倍加持卡Ⅱ'
        PROB_DATA[plugin_configs["SIGN_CARD1_PROB"]['value']]='好感度双倍加持卡Ⅰ'
        
    rand = random.random() - impression / 1000
    for prob in PROB_DATA.keys():
        if rand <= prob:
            return PROB_DATA[prob], 'props'
    gold = random.randint(1, random.randint(1, int(1 if impression < 1 else impression)))
    max_sign_gold = plugin_configs["MAX_SIGN_GOLD"]['value']
    gold = max_sign_gold if gold > max_sign_gold else gold
    return gold, 'gold'





