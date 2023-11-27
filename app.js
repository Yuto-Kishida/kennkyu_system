/* app.js：サーバーサイドスクリプト
目的：
localhost:8000上でページを開けるようにサーバを起動
Juliusから受け取ったデータ情報をCSVファイルに書き込み

*/


//ライブラリの指定
const server = require('ws').Server;
const s = new server({port:8080});
const express = require('express');
const app = express();
const path = require('path');
const helmet = require('helmet');
const createCsvWriter = require('csv-writer').createObjectCsvWriter
const date = require('date-utils')

app.set('views', path.join(__dirname, '/views'));
app.use(express.static(path.join(__dirname, 'public'), {dotfiles: 'allow'}));
app.use('/.well-known',express.static(".well-known"));

//csv書き込み設定
const csvWriter = createCsvWriter({
    path: './log.csv',
    header: ['time','comment','name'],
    encoding:'utf8',
    append: true
})


//websocketを用いたデータ受け取り
let idCounter = 0
s.on('connection', ws => {
    ws.on('message', message => {

        //JSONのParse
        if(message !== null){
            json = JSON.parse(message)
            console.log(json);
        }

        //経過時間
        let now = new Date();
        let formatted = now.toFormat("YYYYMMDDHH24MISS");

        //CSV書き込み
        writeData = [{time:formatted, comment:json.user.data, name:json.user.name}];
        csvWriter.writeRecords(writeData)
        .then(() => {

            //clientにJSONデータを送信
            s.clients.forEach(function(client){
                send_json = JSON.stringify(json)
                client.send(send_json);
            })
        idCounter++;
        });
    });

    ws.on('close', () => {
        console.log('I lost a client');
    });
});


//index.htmlを表示させるための処理
app.get('/',(req,res,next) => {
    res.sendFile(__dirname +'/views/index.html');
    console.log(req.query.language);
})
app.listen(process.env.PORT || 8000);