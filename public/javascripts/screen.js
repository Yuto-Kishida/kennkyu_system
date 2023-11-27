//ライブラリ定義
//import { createRequire } from 'module';
//const { text } = require("express");

//const uri = 'ws://52.194.28.27:8080';
const uri = 'ws://localhost:8080';
const button01 = document.getElementById("button01");
const video = document.querySelector('video');
let header = document.querySelector('header');

//URLのパラメータを変えることで言語指定を行う(localhost:8000/? language = spanish)
let language = "japanese";
let param = new URL(document.location).searchParams;
if (param.get('language')){
  language = param.get('language')
}
console.log(language);

//コメント用画像・フォントサイズ
//let word = ['../gif_text/hayai2.gif',"../gif_text/osoi2.gif","../gif_text/goodp.gif","../gif_text/tired2.gif","../first_text/can2.png","../gif_text/difficult.gif","../gif_text/year.gif","../first_text/fu.png"]
//console.log(word);
let word = ["/firsttext/first.png", "/firsttext/slow.png","/firsttext/good.png","/firsttext/tired.png","/firsttext/can.png","/firsttext/difficult.png","/firsttext/year.png","/firsttext/nice.png","/firsttext/fight.png","/firsttext/yorosiku-1.png", "/firsttext/thankyou.png"];
let secondWord = ['../second_text/first_level2.png',"../second_text/slow_level2.png","../second_text/good_level2.png","../second_text/tired_level2.png","../second_text/can_level2.png","../second_text/difficult_level2.png","../second_text/year_level2.png","../second_text/fu_level2.png"]
let fontSize = [[300,200],[300,200],[300,200],[300,200],[300,200],[300,200],[300,200],[300,200],[300,200],[300,200],[300,200]] //オリジナルサイズ　「速い」:[308, 146], 「遅い」:[349, 134], 「疲れた」:[300, 200], 「まだいける」:[456,111], 「うまくできた」:[451,128], 「難しい」:[459,102], 「イエーイ」:[341, 100]
let fontSize2 = [[232,157],[405,117],[456,121],[405,133],[543,170],[557,116],[519,117],[423,125]]
var player ={"RED": "../" + language + "/firsttext/red3.png", "BLUE":"../" + language + "/firsttext/blue3.png", "GREEN":"../" + language + "/firsttext/green3.png", "YELLOW":"../" + language + "/firsttext/yellow3.png", "kishida":"../" + language + "/firsttext/purple3.png","red_everyone":"../" + language + "/firsttext/new_red-every.png","blue_everyone":"../" + language + "/firsttext/new_blue-every.png","green_everyone":"../" + language + "/firsttext/new_green-every.png","yellow_everyone": "../" + language + "/firsttext/new_yellow-every.png","purple_everyone":"../" + language + "/firsttext/new_purple-every.png","res_blue":"../" + language + "/firsttext/response_blue3.png","res_red":"../" + language + "/firsttext/response_red3.png","res_green":"../" + language + "/firsttext/response_green.png","res_yellow":"../" + language + "/firsttext/response_yellow3.png","res_purple":"../" + language + "/firsttext/response_purple3.png"};
//var response = {9:"../" + language + "response_ex.png"}

//変数定義
let count = 0;
let commentManager = []
let nameManager = []
let flagManager = [false,false,false,false,false,false,false,false,false,false,false]
let loopCount = [0,0,0,0,0,0,0,0,0,0]
let Yes_Count = 0;
let No_Count = 0;
let tempName = "";
let tempCommand = 0;
let Qre_flag = false;
let Qre_flag2 = false;
let participant = new Array();
let userName = ""; //ユーザーの名前であるuserNameを定義
let resEveryone_flag = false;
let resRed_flag = false;
let resBlue_flag = false;
let resGreen_flag = false;
let resYellow_flag = false;
let resPurple_flag = false;


//Socketの処理
window.onload = function () {
  connection = new WebSocket(uri);
  connection.onopen = onOpen;
  connection.onmessage = onMessage;
} 

function onOpen(event) {
  console.log("Connect successful!");
}

function onMessage(event) {
  console.log(event.data);
  let obj = JSON.parse(event.data);
  let command = obj.user.data;
  let name = obj.user.name;
  userName  = name; //ローカル変数であるnameをグローバル変数であるuserNameに代入
  console.log("commnad: " + command + name);
  switch (command){
  
    /*case 6:
      //いぇーい と YESの誤認識を防ぐ為
      textLoop(command,name)
      if (participant.indexOf(name) === -1 && Qre_flag){
        participant.push(name);
        Yes_Count++;
        drawCanvas()
        console.log("はい");
      }      
      */
    // case 9:
    //  resEveryone_flag = true;
    //   textLoop(command,name);
    //   console.log(resEveryone_flag = true")
    //   break;
    case 11:
      textLoop(8,name);
      resEveryone_flag = true;
      break;
    case 12:
      textLoop(2,name);
      resEveryone_flag = true;
      break;
    case 13:
      textLoop(7, name);
      resEveryone_flag = true;
      break;
    case 14:
      textLoop(6,name);
      resEveryone_flag = true;
      break;  
    case 15:
      textLoop(4,name);
      resEveryone_flag = true;
      break;  
    case 16:
      //YESの処理
      if (participant.indexOf(name) === -1 && Qre_flag){
        participant.push(name);
        Yes_Count++;
        drawCanvas()
        console.log("はい");
      }
      break;
    case 17:
      //NOの処理
      if (participant.indexOf(name) === -1 && Qre_flag){
        participant.push(name);
        No_Count++;
        drawCanvas()
        console.log("いいえ")
      }
      break;
    case 18:
      textLoop(10, name);
      resEveryone_flag = true;
      break;
    case 21:
      textLoop(8, name);
      resBlue_flag = true;
      break;
    case 22:
      textLoop(2, name);
      resBlue_flag = true;
      break;
    case 23:
      textLoop(7, name);
      resBlue_flag = true;
      break;
    case 24:
      textLoop(6, name);
      resBlue_flag = true;
      break;
    case 25:
      textLoop(10, name);
      resBlue_flag = true;
      break;
    case 31:
      textLoop(8, name);
      resRed_flag = true;
      break;
    case 32:
      textLoop(2,name);
      resRed_flag = true;
      break;
    case 33:
      textLoop(7, name);
      resRed_flag = true;
      break;
    case 34:
      textLoop(6,name);
      resRed_flag = true;
      break; 
    case 35:
      textLoop(10,name);
      resRed_flag = true;
      break;    
    case 41:
      textLoop(8, name);
      resGreen_flag = true;
      break;
    case 42:
      textLoop(2,name);
      resGreen_flag = true;
      break;
    case 43:
      textLoop(7, name);
      resGreen_flag = true;
      break;
    case 44:
      textLoop(6,name);
      resGreen_flag = true;
      break;
    case 45:
      textLoop(10,name);
      resGreen_flag = true;
      break;
    case 51:
      textLoop(8, name);
      resYellow_flag = true;
      break;
    case 52:
      textLoop(2,name);
      resYellow_flag = true;
      break;
    case 53:
      textLoop(7, name);
      resYellow_flag = true;
      break;
    case 54:
      textLoop(6,name);
      resYellow_flag = true;
      break;
    case 55:
      textLoop(10,name);
      resYellow_flag = true;
      break;   
    case 61:
      textLoop(8, name);
      resPurple_flag = true;
      break;
    case 62:
      textLoop(2,name);
      resPurple_flag = true;
      break;
    case 63:
      textLoop(7, name);
      resPurple_flag = true;
      break;
    case 64:
      textLoop(6,name);
      resPurple_flag = true;
      break;
    case 65:
      textLoop(10,name);
      resPurple_flag = true;
      break;        
    default:
      textLoop(command,name);
      break;
  }
}

document.onkeydown = event =>{
  if (event.key === "0"){
    textLoop(0,"A");
  }else if(event.key === "1"){
    textLoop(1,resEveryone_flag = true );
  }else if(event.key === "2"){
    textLoop(2, resEveryone_flag = true);
  }else if(event.key === "3"){
    textLoop(3, resEveryone_flag = true);
  }else if(event.key === "4"){
    textLoop(4, resEveryone_flag = true)
  }else if(event.key === "5"){
    textLoop(5, resEveryone_flag = true);
  }else if(event.key === "6"){
    textLoop(6, resEveryone_flag = true);
  }else if(event.key === "7"){
    textLoop(7,resEveryone_flag = true);
  }else if(event.key === "8"){
    textLoop(8,resEveryone_flag = true);
  }else if(event.key === "9"){
    textLoop(9,resEveryone_flag = true);
  }else if(event.key === "a"){
    textLoop(10,resEveryone_flag = true);
  }
};

//loopする度にwordSizeを増やす
function textLoop(command,name){
  if(flagManager[command] === false){
    flagManager[command] = true;
    window.setTimeout(function(){
      CommentScreen(command,loopCount[command],name)
      flagManager[command] = false
      loopCount[command] = 0
    });
    // ディレイを入れる時は2000位を目安に
    //console.log("進化するよ");
  }else {
    console.log("カウント");
    loopCount[command]++;
  }
}

//コメント出力時
async function CommentScreen(get_text,wordSize){
  console.log(get_text);
  let img_element = document.createElement('img');
  let div_text = document.createElement("div");
  //let div_element = document.createElement("div"); //text_elementのdivタグ
  let text_element = document.createElement('img');
  text_element.src = player[userName]; 
  console.log(player[userName] + " " + userName)
  text_element.width = 0.5 * fontSize[get_text][0]
  text_element.height = 0.5 * fontSize[get_text][1] 
  div_text.appendChild(text_element);
  //caseごとにレスポンスのdiv要素を追加
  if(resEveryone_flag){
    if(userName == "RED"){
      console.log("redからみんなに対して")
      let res_element = document.createElement('img');
      res_element.src = player["red_everyone"] 
      res_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
      res_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
      div_text.appendChild(res_element);
      resEveryone_flag = false;
    }else if(userName == "BLUE"){
      console.log("blueからみんなに対して")
      let res_element = document.createElement('img');
      res_element.src = player["blue_everyone"] 
      res_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
      res_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
      div_text.appendChild(res_element);
      resEveryone_flag = false;
    }else if(userName == "GREEN"){
      console.log("greenからみんなに対して")
      let res_element = document.createElement('img');
      res_element.src = player["green_everyone"] 
      res_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
      res_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
      div_text.appendChild(res_element);
      resEveryone_flag = false;
    }else if(userName == "YELLOW"){
      console.log("yellowからみんなに対して")
      let res_element = document.createElement('img');
      res_element.src = player["yellow_everyone"] 
      res_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
      res_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
      div_text.appendChild(res_element);
      resEveryone_flag = false;
    }else if(userName == "kishida"){
      console.log("purpleからみんなに対して")
      let res_element = document.createElement('img');
      res_element.src = player["purple_everyone"] 
      res_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
      res_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
      div_text.appendChild(res_element);
      resEveryone_flag = false;
    }
  }else if(resBlue_flag){
    console.log("blueに対して")
    let resBlue_element = document.createElement('img');
    resBlue_element.src = player["res_blue"] 
    resBlue_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
    resBlue_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
    div_text.appendChild(resBlue_element);
    resBlue_flag = false;
  }else if(resRed_flag){
    console.log("Redに対して")
    let resRed_element = document.createElement('img');
    resRed_element.src = player["res_red"] 
    resRed_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
    resRed_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
    div_text.appendChild(resRed_element);
    resRed_flag = false;
  }else if(resGreen_flag){
    console.log("Greenに対して")
    let resGreen_element = document.createElement('img');
    resGreen_element.src = player["res_green"] 
    resGreen_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
    resGreen_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
    div_text.appendChild(resGreen_element);
    resGreen_flag = false;
  }else if(resYellow_flag){
    console.log("yellowに対して")
    let resYellow_element = document.createElement('img');
    resYellow_element.src = player["res_yellow"] 
    resYellow_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
    resYellow_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
    div_text.appendChild(resYellow_element);
    resYellow_flag = false;
  }else if(resPurple_flag){
    console.log("Purpleに対して")
    let resPurple_element = document.createElement('img');
    resPurple_element.src = player["res_purple"] 
    resPurple_element.width = 0.6 * fontSize[get_text][0]//[0]はfontsizeの配列1つ目[300,300](300)
    resPurple_element.height = 0.6 * fontSize[get_text][1]//[1]はfontsizeの配列2つ目[300,300](300)
    div_text.appendChild(resPurple_element);
    resPurple_flag = false;
  }
  
  //コメント進化処理
  //コメントの言語指定とワードに対するサイズの設定
  if(wordSize < 2){
    img_element.src = "../" + language + word[get_text]; // 画像パス(languageは言語パス)    
    img_element.width = 0.8 * fontSize[get_text][0]
    img_element.height = 0.8 * fontSize[get_text][1] 
  }
  // else{
  //   img_element.src = secondWord[get_text];
  //   img_element.width = 1.0 * fontSize2[get_text][0]
  //   img_element.height = 1.0 * fontSize2[get_text][1] 
  // }
  
  //画面上にコメントを流す設定
  count++;
  div_text.id = "text" + count;
  div_text.style.position = 'fixed';
  div_text.style.whiteSpace = 'nowrap';
  div_text.style.fontSize = wordSize + 'px';
  div_text.style.color = 'white'
  div_text.className = "text"

  // div_element.id = "element" + count;
  // div_element.style.position = 'fixed';
  // div_element.style.whiteSpace = 'nowrap';
  // div_element.style.fontSize = 'px';
  // div_element.style.color = 'white'
  // div_element.className = "element"

  div_text.style.left = (document.documentElement.clientWidth) + "px";
  // div_element.style.left = (document.documentElement.clientWidth) + "px";
  let random = (Math.random() * 0.81) + 0.08;
  let topRandom = Math.round(random * (document.documentElement.clientHeight));
  console.log(random);
  div_text.style.top = topRandom + 'px';
  //div_element.style.top = topRandom + 'px';
  div_text.appendChild(img_element); 
  //div_text.appendChild(text_element);
  document.body.appendChild(div_text);
  //div_text.appendChild(div_element);
 
  await gsap.to("#" + div_text.id, {duration:8,x: -1 * (document.documentElement.clientWidth+div_text.clientWidth)});
  if(document.getElementById(div_text.id) != null){
    div_text.parentNode.removeChild(div_text);
  }
  // await gsap.to("#" + div_element.id, {duration:8,x: -1 * (document.documentElement.clientWidth+div_element.clientWidth)});
  // if(document.getElementById(div_element.id) != null){
  //   div_element.parentNode.removeChild(div_element);
  // }
}


//コマンド選択用の関数
function CommandSelect(number){
  let printText
  printText = word[number];
  flagManager[number] = false;
  return printText;
}

//アンケート機能の処理
document.addEventListener("keydown", event => {
  if (event.key === "Escape"){
    console.log("YES/NO開始")
    header.style.visibility ="visible";
    Qre_flag = true;
    window.setTimeout(function(){
      clearCanvas();
      console.log("YES/NO終了")
    },15000)
  }
});


//アンケート機能画面表示機能
function drawCanvas(){
  let allCount = 0;
  allCount = Yes_Count + No_Count;
  console.log("allCount: "+ allCount);
  let yesAnswer = Math.round(Yes_Count / allCount * 100);
  let noAnswer = Math.round(No_Count / allCount * 100); 
  document.getElementsByClassName("contain")[0].style.visibility = "visible";
  document.getElementsByClassName("item1")[0].style.width = yesAnswer + "%";
  document.getElementsByClassName("item2")[0].style.width = noAnswer + "%";
  document.getElementsByClassName("item1")[0].innerHTML = "YES" + String(Yes_Count) + "人";
  document.getElementsByClassName("item2")[0].innerHTML = "NO:" + String(No_Count) + "人";
}

//アンケート機能起動後初期化
function clearCanvas(){
  yesAnswer = 0;
  noAnswer = 0;
  document.getElementsByClassName("contain")[0].style.visibility = "hidden";
  document.getElementsByClassName("item1")[0].style.width = yesAnswer + "%";
  document.getElementsByClassName("item2")[0].style.width = noAnswer + "%";
  document.getElementsByClassName("item1")[0].innerHTML = "";
  document.getElementsByClassName("item2")[0].innerHTML = "";
  Yes_Count=0;
  No_Count=0;
  participant = [];
  Qre_flag = false;
  header.style.visibility ="hidden";
}