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
    ・screen.js：コメント流れる処理
  ・stylesheets
    ・top.css：大体全部のcss
log.csv：コメントのログファイル
index.html：表示画面


google_speech_recognizer説明

目的：
１：音声認識のフィルタリング、閾値の設定
　→特定のコメント以外は反応しないように設定
２：音声認識されたコメントデータの送信

本システムで使用されるのはgoogle_speech_recognizer jp.py

