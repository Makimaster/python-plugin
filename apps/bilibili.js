import { segment } from "oicq";
import {createRequire} from "module";
import fs from "fs";
const require = createRequire(import.meta.url);
//项目路径

const _path = process.cwd();

export async function bilibilidingyue(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['订阅']=='关闭'){return false;}
  }
	let args=''
	if (e.msg.includes('up')||e.msg.includes('UP'))args='up';
	if (e.msg.includes('番剧')||e.msg.includes('动漫'))args='番剧';
  if (e.msg.includes('直播'))args='直播';
	if(args=='')return false;
  let uid=e.msg.match(/(\d+)/g)
  if(!uid)return false;
  uid=uid[0];
  let command = "python ./plugins/python-plugin/py/bilibili/bilibili-dingyue.py "+' '+e.group_id+' '+uid+' '+args;
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else if(stdout.trim()=="already"){
    		e.reply("本群已订阅")
        return false;
    	}else if(stdout.trim()=="requesterror"){
    		e.reply("未查到此UID")
        return false;
    	}else{
    		let list = JSON.parse(fs.readFileSync(`${_path}//plugins/python-plugin/data/bilibili.json`, "utf8"));
    		let key=stdout.trim().toString();
        let name=list[key].uname
      	e.reply("订阅"+name+"成功")
        return false;
    }
  })
}

export async function bilibilisoufan(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['订阅']=='关闭'){return false;}
  }
  let msg1 =e.msg.replace(/#|\;|cat|tac| |\\$|\*|>|more|less|net|head|sort|tail|sed|cut|awk|strings|od|curl|搜番|\`|\\%|\\&|\||/g, "");
  if(!msg1){return false;}
  let command = "python ./plugins/python-plugin/py/bilibili/bilibili_soufan.py "+' '+msg1;
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{
    	let list = JSON.parse(fs.readFileSync(`${_path}//plugins/python-plugin/data/soufan.json`, "utf8"));
    	var data =Object.keys(list)  
        let bilibili=[];
  		for (var key of data){
      		
      		bilibili.push('番名：'+list[key].title+'uid:'+list[key].media_id)
            
        };
  		if(!bilibili[0]){
  			e.reply('未搜索到番剧')
        return false;
  		}else{
  			e.reply(bilibili)}
        return false;
   	 	}
  		})
}

export async function bilibililist(e) {
  if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['订阅']=='关闭'){return false;}
  }
	  if (!fs.existsSync(`./plugins/python-plugin/data/bilibili.json`)) {
         return;}
  let list = JSON.parse(fs.readFileSync(`${_path}//plugins/python-plugin/data/bilibili.json`, "utf8"));
  var data =Object.keys(list)
  let bilibili=[];
  for (var key of data){
      if (list[key].gid.toString()==e.group_id.toString()){

      	bilibili.push('名字：'+list[key].uname+'uid：'+list[key].uid)
        //bilibili.push('\n')
            
        }};
  if(!bilibili[0]){
  	e.reply('本群未订阅')
  }else{
  e.reply(bilibili.join(',').replace(/,/g,'\n'))
  return false;
}
    
}
export async function bilibilidelete(e) {
	if (fs.existsSync(`./plugins/python-plugin/data/cfg.json`)) {
    let cfg = JSON.parse(fs.readFileSync(`./plugins/python-plugin/data/cfg.json`, "utf8"));
    if(cfg['订阅']=='关闭'){return false;}
  }
  let uid=e.msg.match(/(\d+)/g)[0]
  let command = "python ./plugins/python-plugin/py/bilibili/bilibili-dingyue.py "+' '+e.group_id+' '+uid+' 删除';
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
      return false;
    }else if(stdout.trim()=="empty"){
    		e.reply("本群未订阅")
        return false;
    	}else if(stdout.trim()=="success"){
    		e.reply("删除订阅成功")
        return false;
    	}
    })
}