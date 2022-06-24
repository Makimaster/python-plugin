import { segment } from "oicq";
import fetch from "node-fetch";
import fs from "fs";
import lodash from "lodash";
import {createRequire} from "module";
//项目路径
import { exec } from "child_process";
const _path = process.cwd();
const require = createRequire(import.meta.url);
export async function life(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['人生重来']=='关闭'){return false;}
  }
  //console.log(e.nickname)
  let msg1 =e.nickname.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||分配|/g, "");
  let command = "python ./plugins/python-plugin/py/lifeRestart/liferestart.py "+msg1+' '+e.user_id;
  //var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/life/${e.user_id}.png`),
        ];
      e.reply(msg)
      return false;
    }
  })

}


//接受天赋

export async function life1(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['remake']=='关闭'){return true;}
  }
  //console.log(e.nickname)
  //let msg1 =e.msg.replace(/#|\;|cat|tac| |[0-9]|\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let msg1 =e.nickname.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let command = "python ./plugins/python-plugin/py/life/liferestart.py "+msg1+' '+e.user_id+' '+'开始'+' '+'abc';
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/life1/${e.user_id}.png`),
        ];
      e.reply(msg)
    }
  })
  return true;
}
//接受天赋

export async function life2(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['remake']=='关闭'){return true;}
  }
  //console.log(e.nickname)
  let msg1 =e.msg.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||选择|/g, "");
  let msg2 =e.nickname.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let command = "python ./plugins/python-plugin/py/life/liferestart.py "+msg2+' '+e.user_id+' '+'天赋'+' '+msg1;
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/life1/${e.user_id}.png`),
        ];
      e.reply(msg)
    }
  })
  return true;
}

//接收
export async function life3(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['remake']=='关闭'){return true;}
  }
  //console.log(e.nickname)
  let msg1 =e.msg.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||分配|/g, "");
  let msg2 =e.nickname.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let command = "python ./plugins/python-plugin/py/life/liferestart.py "+msg2+' '+e.user_id+' '+'属性'+' '+msg1;
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=='error'){
      let msg="输入错误"
      e.reply("输入错误")
    }else{
      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/life1/${e.user_id}.png`),
        ];
      e.reply(msg)
    }}
  })
  return false;
}
let NICKNAME=BotConfig.group.default.botAlias//机器人的名字
export async function sign(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['签到']=='关闭'){return true;}
  }
  //console.log(e.nickname)
  let msg1 =e.nickname.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\\%|\\&|\||/g, "");
  let command = "python ./plugins/python-plugin/py/sign/sign.py "+msg1+' '+e.user_id+' '+NICKNAME;
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
      if (stdout.trim()=='error'){
      let msg="输入错误"
      e.reply("输入错误")
    }else{
      let msg = [
        segment.image(`file:///${_path}/plugins/python-plugin/resrouces/today_card/${e.user_id}.png`),
        ];
      e.reply(msg)
    }}
  })
  return false;
}
