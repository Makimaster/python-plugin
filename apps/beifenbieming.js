import fs from 'fs';
import {segment} from "oicq";
const _path = process.cwd();
import path from 'path';
const __dirname = path.resolve();

export async function beifen(){
	
	let genshin = await import(`file://${_path}/config/genshin/roleId.js`);

	let new_genshin = await import(`file://${_path}/config/genshin/roleId_list.js`);

	let roleId =YunzaiApps.mysInfo.init(true);
	let str = fs.readFileSync(__dirname + "/config/genshin/roleId.js", "utf8");
	//var pattern =/^let roleId = [\s\S]+?;$/m;
	var roleId_new1 = new_genshin.roleId;
	var roleId_new2 = genshin.roleId
	var data =Object.keys(roleId_new1)
	
	for (var key of data){
		for (var key1 of roleId_new1[key]){
			if (!roleId_new2[key].includes(key1)){
				roleId_new2[parseInt(key)].push(key1)
			}
		}

		var pattern =key.toString()+": [[]{1}(.+)]";
		var test=str.match(pattern)
		console.log(test)	
		str=str.replace(test,"\""+roleId_new2[parseInt(key)].join(",").replace(/,/g,"\",\"")+"\"");
		
	}
	fs.writeFileSync(__dirname + "/config/genshin/roleId.js",str, 'utf8')
	roleId =YunzaiApps.mysInfo.init(true);
	return false;
}