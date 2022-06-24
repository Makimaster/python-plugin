import { segment } from "oicq";
import fetch from "node-fetch";
import fs from "fs";
import { exec } from "child_process";
import { pipeline } from "stream";
import common from "../../../lib/common.js";
import { promisify } from "util";
import {createRequire} from "module";
//import { getlog } from "../../../lib/app/gachaLog.js"
const require = createRequire(import.meta.url);
//项目路径
const _path = process.cwd();

Bot.on("message.private",async (e) => {
  if (!e.file || !e.file?.name.includes("xls")) {
    return;
  }
  let uid=e.file.name.match(/(\d+)/g)
  if (!uid[0])return;
  let path = "data/file/";

  if (!fs.existsSync(path)) {
    fs.mkdirSync(path);
  }
  if (!fs.existsSync(`${path}output_log/`)) {
    fs.mkdirSync(`${path}output_log/`);
  }

  let textPath = `${path}output_log/${e.user_id}.xlsx`;

  //获取文件下载链接
  let fileUrl = await e.friend.getFileUrl(e.file.fid);
  //下载output_log.txt文件
  const response = await fetch(fileUrl);
  const streamPipeline = promisify(pipeline);
  await streamPipeline(response.body, fs.createWriteStream(textPath));

  //读取txt文件
  //let txt = fs.readFileSync(textPath, "utf-8");
  //let url = txt.match(/auth_appid=webview_gacha(.*)hk4e_cn/);


  common.relpyPrivate(e.user_id, "文件发送成功,数据生成中。。");
  let command = "python ./plugins/python-plugin/py/gacha.py "+e.user_id+' '+uid;
  var exec = require('child_process').exec;
  //e.group.fs.upload(`${_path}/plugins/python-plugin/resrouces/123.py`)
  var ls =exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else{

      let msg = ["写入json成功，正在生成抽卡记录。。。"     
        ];
      e.reply(msg)
    }
  })
  //删除文件
  //await fs.unlink(textPath, (err) => {
  //});

  //await bing(e);
  //e.msg = "角色记录";
  //await getLog(e);
  return false;
})
let timer;

Bot.on("system.offline.kickoff",async ()=> {

  let command = "python ./plugins/python-plugin/py/huanhao.py";
  var exec = require('child_process').exec;
  var ls = exec(command, function (error, stdout, stderr){
    if (error) {
      console.log("失败！\nError code: "+error.code+"\n"+error.stack);
    }else {
      timer && clearTimeout(timer);
      redis.set("huanhao:restart-msg", JSON.stringify({
      msg: "重启成功，已更换新账号",
      qq: BotConfig.masterQQ[0]
      }), { EX: 30 });
      let command = "npm run restart";
      let lt=exec(command, function (error, stdout, stderr) {
        if (error) {

          if (error) {
            Bot.pickUser(BotConfig.masterQQ[0]).sendMsg("自动重启失败，请手动重启以应用新版python-plugin。请使用 npm run start 命令启动Yunzai-Bot");
          } else {
            Bot.pickUser(BotConfig.masterQQ[0]).sendMsg("重启失败！\nError code: " + error.code + "\n" + error.stack + "\n 请稍后重试。");
          }
          return true;
        }
      })
      
    }
  })
  return true;
})