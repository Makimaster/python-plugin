import { segment } from "oicq";
import fetch from "node-fetch";
import schedule from "node-schedule";
import {createRequire} from "module";
const require = createRequire(import.meta.url);
//项目路径
const _path = process.cwd();

schedule.scheduleJob("0 0 0 * * ?",()=>{
  let command = "python ./plugins/python-plugin/py/clearpic.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }})

});


const checkAuth = async function (e) {
  return await e.checkAuth({
    auth: "master",
    replyMsg: `只有主人才能命令喵喵哦~
    (*/ω＼*)`
  });
}

export async function huangli(e) {
  let command = "python ./plugins/python-plugin/py/almanac.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/qianwen/黄历.png`),
        ];
      e.reply(msg)
    }
  })
  return true;
}
export async function qiuqian(e) {
  let command = "python ./plugins/python-plugin/py/draw_lots.py "+e.user_id;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      let msg = [

        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/qianwen/${e.user_id}.png`),
        ];
      e.reply(msg)
    }
  })
  return true;
}
export async function jieqian(e) {
  let command = "python ./plugins/python-plugin/py/draw_lots.py "+e.user_id;
  const exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout){
        let msg = [

          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/qianwen/${e.user_id}.png`),
          ];
        e.reply(msg)
      }else{
        let msg = [

          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/jieqian/${e.user_id}.png`),
          ];
        e.reply(msg)
      }
      
    }
  })
  return true;
}
export async function qingli(e) {
  if (!await checkAuth(e)) {
    return true;
  }
  let command = "python ./plugins/python-plugin/py/clearpic.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      e.reply("清理成功！")
    }
  })
  return true;
}
export async function food(e) {
  let msg1 =e.msg.replace(/#| |/g, "");
  let command = "python ./plugins/python-plugin/py/fys.py "+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=="error"){
           let msg = ['查无此食物'];
            e.reply(msg)
      }else{
      let msg = [

          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/food/${msg1.substr(2)}.png`),
          ];
        e.reply(msg)     
      
      }}
  })
  return true;
}
export async function enemies(e) {
 let msg1 =e.msg.replace(/#| |/g, "");
  //const iconv=require('iconv-lite');{encoding:'binary'},
  let command = "python ./plugins/python-plugin/py/fys.py "+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack,stdout);
    }else{
      if (stdout.trim()=="error"){
           let msg = ['查无此原魔'];
            e.reply(msg)
      }else{
      let msg = [

          stdout,
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/enemies_info/${msg1.substr(2)}.png`),
          ];
        e.reply(msg)     
      
      }}
  })
  return true;
}
export async function artifacts(e) {
  let msg1 =e.msg.replace(/#| |/g, "");
  //const iconv=require('iconv-lite');
  let command = "python ./plugins/python-plugin/py/fys.py "+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=="error"){
           let msg = ['查无此圣遗物'];
            e.reply(msg)
      }else{
        let msg = [
          stdout,
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/artifacts/${msg1.substr(3)}.png`),
          ];
        e.reply(msg)     
      }
      }
  })
  return true;
}
export async function cailiao(e) {
  let msg1 =e.msg.replace(/#|在|哪|里|有/g, "");
  let n= msg1.match('渊下宫')?7:msg1.match('层岩')?9:2;
  let msg2=(n==7)?msg1.replace(/渊下宫/,''):msg1.replace(/层岩/,'')
  let command = "python ./plugins/python-plugin/py/qrps.py "+msg2+' '+n;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=="error"){
           let msg = ['查无此资源'];
            e.reply(msg)
      }else{
     let msg = [
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/cailiaodian/${msg2}.png`),
          ];
        e.reply(msg)     
      
      }}
  })
  return true;
}

export async function tarot(e) {
  await e.reply("开始洗牌")

  await e.reply("牌洗好了，请从78张卡牌中抽取四张,如：抽取45,67,23,35")     
  return true;
}
export async function tarot1(e) {
  let command = "python ./plugins/python-plugin/py/toro/tarot.py "+e.msg;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
     let msg = [
          segment.image(`file:///${_path}/plugins/python-plugin/resrouces/tarot/torot.png`),
          ];
        e.reply(msg)     
      
      }
  })
  return true;
}

