import { segment } from "oicq";
import fetch from "node-fetch";
import {createRequire} from "module";
const require = createRequire(import.meta.url);
//项目路径
const _path = process.cwd();
//简单应用示例
//帮助：表情帮助

const keywordList = [
  "表情更新",
  "摸",
  "摸摸",
  "摸头",
  "摸摸头",
  "rua",
  "亲",
  "亲亲",
  "贴贴",
  "贴",
  "蹭",
  "蹭蹭",
  "顶",
  "玩",
  "拍",
  "撕",
  "丢",
  "扔",
  "抛",
  "掷",
  "爬",
  "精神支柱",
  "一直",
  "加载中",
  "转",
  "小天使",
  "不要靠近",
  "一样",
  "滚",
  "玩游戏",
  "来玩游戏",
  "膜拜",
  "膜",
  "吃",
  "啃",
  "出警",
  "警察",
  "问问",
  "去问问",
  "舔屏",
  "舔",
  "prpr",
  "搓",
  "国旗",
  "墙纸",
  "交个朋友",
  "继续干活",
  "完美",
  "完美的",
  "关注",
  "我朋友说",
  "我有个朋友说",
  "这像画吗",
  "震惊",
  "兑换券",
  "听音乐",
  "典中典",
  "哈哈镜",
  "永远爱你",
  "对称",
  "安全感",
  "永远喜欢",
  "我永远喜欢",
  "采访",
  "打拳",
  "群青",
  "捣",
  "捶",
  "需要",
  "你可能需要",
  "捂脸",
  "敲",
  "垃圾",
  "垃圾桶",
  "为什么at我",
  "像样的亲亲",
  "啾啾",
  "吸",
  "嗦",
  "紧贴",
  "紧紧贴着",
  "锤",
  "可莉",
  "仰望大佬",
  "打",
  "击剑",
  "mo鱼",
  "赞",
  "小恐龙",
  "吞",
  "胡桃",
  "快逃",
  "色色",
  "踢",
  "踩",
];
const specialList = [
  "摸",
  "摸摸",
  "摸头",
  "摸摸头",
  "rua",
  "撕",
  "爬",
  "小天使",
  "玩游戏",
  "来玩游戏",
  "问问",
  "去问问",
  "交个朋友",
  "关注",
  "我朋友说",
  "我有个朋友说",
  "兑换券",
  "典中典",
  "对称",
  "安全感",
  "采访",
  "永远喜欢",
  "我永远喜欢",
  "表情更新",
];
export async function biaoQing(e) {
  if (!e.isGroup || !e.msg) {
    return false;
  }
  const atItem = e.message.filter((item) => item.type === "at");

  let isSpecial = specialList.filter((item) => e.msg.includes(item) && item !== e.msg).length > 0;
 
  let key = '';
  let target='';
  let flag=0;
if (e.img){target=e.img[0], key=e.msg}
if (e.msg.match('自己')){target=e.user_id; key=e.msg.replace('自己','');}
if (atItem.length){target=atItem[0].qq, key=e.msg}
  if     (!keywordList.includes(e.msg) && !isSpecial && !keywordList.includes(key))
    return false;


  let specialName = isSpecial
    ? getSpecialName(
        key.trim(),
        specialList.filter((item) => key.includes(item) )[0]
      )
    : key;

let cmd = specialName.split('_').shift();

if (e.msg.match('表情更新')){cmd=e.msg.replace('表情更新', '')}
//console.log(target, key);

if (!keywordList.includes(cmd) && !keywordList.includes(e.msg))
  return false;

key =specialName;
if (e.msg.match('表情更新')){key=e.msg.replace('表情更新', 'update_'),target=e.user_id}
//console.log(target, key,master);

if(key=='永远喜欢'&atItem.length){target=atItem[0].text.replace('@','');flag=1}
if(key=='典中典'&atItem.length){target=atItem[0].text.replace('@','');flag=1}
  if (target) {//+e.group_id+' '
    let command = "python ./plugins/python-plugin/py/petpet/petpet.py "+e.user_id+' '+target+' '+key+' '+flag;
    var exec = require('child_process').exec;
    var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      let msg = [
        stdout,
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/images/123.${stdout.trim()}`),
        ];
      e.reply(msg)
    }
    
    return true;
  })}
}
export async function biaoQingHelp(e) {
  if (!e.isGroup) {
    return false;
  } else {
    await e.reply([
      segment.image(`file:///${_path}/plugins/python-plugin/resrouces/images/help.jpeg`),
    ]);
    return true; //返回true 阻挡消息不再往下
  }
}
function getSpecialName(msg, chooseItem) {
  let name = "";
  switch (chooseItem) {
    case "摸":
    case "摸摸":
    case "摸头":
    case "摸摸头":
    case "rua":
      if (msg.includes("圆")) name = msg.replace("圆", "_圆");
      else name = msg.replace("摸", "摸_");
      break;
    case "撕":
      if (msg.includes("滑稽")) name = msg.replace("滑稽", "_滑稽_");
      else name = msg.replace("撕", "撕_");
      break;
    case "爬":
      if (/\d+/.test(msg)) name = msg.replace(/\d+/, `_${msg.match(/\d+/)[0]}_`);
      else name = msg.replace("摸", "摸_");
      break;
    case "小天使":
      if (msg.includes("自己")) name = msg.replace("小天使", "小天使_").replace("自己", "_自己");
      else name = msg.replace("小天使", "小天使_");
      break;
    case "玩游戏":
    case "来玩游戏":
      name = msg.replace("玩游戏", "玩游戏_");
      break;
    case "问问":
    case "去问问":
      name = msg.replace("问问", "问问_");
      break;
    case "交个朋友":
      name = msg.replace("交个朋友", "交个朋友_");
      break;
    case "关注":
      name = msg.replace("关注", "关注_");
      break;
    case "我朋友说":
    case "我有个朋友说":
      name = msg.replace("朋友说", "朋友说_").replace("自己", "_自己");
      break;
    case "兑换券":
      name = msg.replace("兑换券", "兑换券_");
      break;
    case "典中典":
      if (msg.includes("彩")) name = msg.replace("彩", "_彩_");
      else name = msg.replace("典中典", "典中典_");
      break;
    case "对称":
      if (/(上|下|左|右)/.test(msg))
        name = msg.replace(/(上|下|左|右)/, `_${msg.match(/(上|下|左|右)/)[0]}`);
      else name = "对称";
      break;
    case "安全感":
      name = msg.replace("安全感", "安全感_");
      break;
    case "采访":
      name = msg.replace("采访", "采访_");
      break;
    case "永远喜欢":
    case "我永远喜欢":
      name = msg.replace("永远喜欢", "永远喜欢_");
      break;
  }
  return name;
}





