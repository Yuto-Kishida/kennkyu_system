node_websocket説明

目的：
参加者から受け取ったデータを画面上に表示
そのために
１：サーバの立ち上げ・コメントの受け取り
２：受け取ったデータをニコ生風に表示する

app.js：localhostサーバ立ち上げ・websocket受け取り用
node_modules：ダウンロードしたライブラリ(node.jsの使用) 
package.json：インストールリスト(システム動作には関係なし)
public：システムの表示に関わるファイル
  ・first_text：コメントLeveL1の画像ファイル
  ・second_text：コメントLeveL2の画像ファイル
  ・javascript
    ・explosion.js：爆発処理
    ・screen.js：コメント流れる処理
  ・stylesheets
    ・top.css：大体全部のcss
    ・explosion.css：爆発に関するcss
log.csv：コメントのログファイル
index.html：表示画面
