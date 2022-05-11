import {
  huangli,
  qiuqian,
  jieqian,
  food,
  enemies,
  artifacts,
  qingli,
  cailiao,
  tarot,
  tarot1
} from "./apps/huangli.js";
import {
  biaoQing,
  biaoQingHelp
} from "./apps/petpet.js";
import lodash from "lodash";
import common from "../../lib/common.js";
export {
  huangli,
  qiuqian,
  jieqian,
  food,
  enemies,
  artifacts,
  qingli,
  cailiao,
  tarot,
  tarot1,
  biaoQing,
  biaoQingHelp
};
let rule = {
  huangli: {
    reg: "^#(黄历|日历)$", //匹配消息正则，命令正则
    describe: "【#黄历】今日迷信", //【命令】功能说明
  },
  qiuqian: {
    reg: "^#(求签)$", //匹配消息正则，命令正则

    describe: "【#求签】今日运势", //【命令】功能说明
  },
  jieqian: {
    reg: "^#(解签)$", //匹配消息正则，命令正则

    describe: "【#解签】进行解签", //【命令】功能说明
  },
  food: {
    reg: "^#(食物).*$", //匹配消息正则，命令正则

    describe: "【#食物】获取食物信息", //【命令】功能说明
  },
  enemies: {
    reg: "^#(原魔).*$", //匹配消息正则，命令正则

    describe: "【#原魔】获取食物信息", //【命令】功能说明
  },
  artifacts: {
    reg: "^#(圣遗物).*$", //匹配消息正则，命令正则

    describe: "【#圣遗物】获取圣遗物信息", //【命令】功能说明
  },
  qingli: {
    reg: "^#(清理签文)$", //匹配消息正则，命令正则

    describe: "【#清理签文】清空所有签文", //【命令】功能说明
  },
  cailiao: {
    reg: "^#.*(在哪|在哪里|哪有|哪里有)$", //匹配消息正则，命令正则

    describe: "【材料名在哪|在哪里|哪有|哪里有】返回一张地图", //【命令】功能说明
  },
  tarot: {
    reg: "^#(塔罗牌).*$", //匹配消息正则，命令正则

    describe: "【算命】计算今日运势", //【命令】功能说明
  },
  tarot1: {
    reg: "^(抽取).*$", //匹配消息正则，命令正则

    describe: "抽取塔罗牌", //【命令】功能说明
  },
   biaoQing: {
    reg: "noCheck", //匹配消息正则，命令正则

    describe: "头像表情包", //【命令】功能说明
  },
  biaoQingHelp: {
    reg: "^表情帮助$", //匹配消息正则，命令正则
    describe: "表情帮助", //【命令】功能说明
  },
};

lodash.forEach(rule, (r) => {
  r.priority = r.priority || 50;
  r.prehash = true;
  r.hashMark = true;
});
export { rule };
