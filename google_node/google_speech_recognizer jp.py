#Synchronous Recognition, limited to a minute or Less
#480 hours of audio per day
#900 requests per 60 seconds
#https://cloud.google.com/speech-to-text/quotas
#from dis import _HaveCodeOrStringType
from operator import truediv
from unicodedata import name
import speech_recognition as s_r
import json
from websocket import create_connection
import socket
import time
import timeit
#import threading

start_time = time.time()
# json_list = {
#     "key" : [] 
# }
json_data = {
    "user":{"name":"","data":"1"}
}
host = socket.gethostname() #gethostnameはPCのhostnameを取得してくる
print(host)
json_list = []

#HOST = '127.0.0.1'   # juliusサーバーのIPアドレス
#PORT = 10500         #juliusサーバーの待ち受けポート
#DATESIZE = 1024     # 受信データバイト数

# def add_websocket(number,name):
#         json_data['user']['data'] = str(number)
#         json_data['user']['name'] = host #host or socket.gethostname
#         json_str = json.dumps(json_data)
#         json_list.append(json_str)
#         #ws = create_connection("ws://52.194.28.27:8080")

# def send_websocket(new_str):        
#         ws = create_connection("ws://127.0.0.1:8080")
#         new_str = json_list
#         ws.send(new_str)
#         # response = ws.recv()
#         # print(response)
#         ws.close()

def websocket(number,name):
    json_data['user']['data'] = number
    json_data['user']['name'] = socket.gethostname()
    json_str = json.dumps(json_data)
    #ws = create_connection("ws://52.194.28.27:8080")
    ws = create_connection("ws://127.0.0.1:8080")
    
    ws.send(json_str)
    response = ws.recv()
    print(response)
    ws.close()

r = s_r.Recognizer()
mic = s_r.Microphone()
word_list = ["よろしく","早い","アイアイ", "遅い","まだいける","疲れた","うまくできた","難しい","イエーイ","ありがとう","イエス","YES","yes","ノー","NO","No","ニュース","はい", "YEAH","の","いいね","頑張ろう","いいえ","家","まだ行ける","頑張れ","みんな頑張れ","みんながんばれ","みんながんばろう","がんばれみんな","みんな頑張ろう","頑張ろうみんな","がんばろうみんな","みんなまだいける","まだいけるみんな","みんな まだ行ける","みんな まだいける","みんないいね","いいねみんな","みんなイエーイ","イエーイみんな","みんなうまくできた","みんなありがとう","青がんばれ","青 がんばろ","あおがんばろう","がんばろう 青","頑張ろう 青","頑張ろうあお","青 頑張ろう","あお頑張ろう","青 まだいける","あおまだいける","まだいける 青","まだいけるあお","青 いいね","あおいいね","もう いいね","青いね","青い犬","青 イエーイ","あおイエーイ","イエーイ 青","イエーイあお","青ありがとう","花をありがとう","パオ ありがとう","真央 ありがとう","あと頑張れ","あと 頑張れ","赤 頑張れ","赤 頑張ろう","赤 がんばろう","赤 まだいける","あか まだいける","袴田 行ける","赤 いいね","赤いいね","あか いいね","赤イエーイ","あかいえーい","アカ ありがとう","アク ありがとう","赤ありがとう","みどり 頑張れ","緑 頑張れ","緑 頑張ろう","みどり 頑張ろう","みどり がんばろう","緑 がんばろう","緑 まだいける","みどり まだいける","緑 いいね","みどり いいね","緑イエーイ","みどりイエーイ","ミドリ ありがとう","緑ありがとう","黄色 頑張れ","黄色 頑張ろう","黄色 がんばろう","黄色 まだいける","きいろ まだいける","黄色 いいね","黄色いいね","きいろ いいね","黄色イエーイ","きいろイエーイ","黄色 ありがとう","ヒーローありがとう","紫 頑張れ","紫 頑張ろう","紫 がんばろう""紫 まだいける","むらさき まだいける","紫 いいね","むらさき いいね","紫イエーイ","むらさきイエーイ","紫 ありがとう",] #ストップ, 疲れた
wordNumber_list = {"早い":0,"アイアイ":0, "遅い":1,"まだいける":2,"まだ行ける":2,"疲れた":3,"うまくできた":4,"難しい":5,"イエーイ":6,"ありがとう":10,"よろしく":9,"YEAH":6,"Yeah":6,"イエス":16,"ノー":17,"YES":16,"NO":17,"No":17,"いいえ":17,"家":17,"yes":16,"ニュース":16,"はい":16,"の":17,"いいね":7,"頑張ろう":8,"頑張れ":8,"みんながんばれ":11,"みんな頑張れ":11,"みんながんばろう":11,"がんばれみんな":11,"みんな頑張ろう":11,"頑張ろうみんな":11,"がんばろうみんな":11,"みんなまだいける":12,"みんな まだ行ける":12,"みんな まだいける":12,"まだいけるみんな":12,"みんないいね":13,"いいねみんな":13,"みんなイエーイ":14,"イエーイみんな":14,"みんなうまくできた":15,"みんなありがとう":18,"青がんばれ":21,"青 がんばろ":21,"あおがんばろ":21,"がんばろう 青":21,"がんばろあお":21,"青 頑張ろう":21,"あお頑張ろう":21,"頑張ろう 青":21,"頑張ろうあお":21,"青 まだいける":22,"青ありがとう":25,"花をありがとう":25,"パオ ありがとう":25,"真央 ありがとう":25,"あおまだいける":22,"まだいける 青":22,"まだいけるあお":22,"青 いいね":23,"もう いいね":23,"青いね":23,"青い犬":23,"青 イエーイ":24,"あおイエーイ":24,"イエーイ 青":24,"イエーイあお":24,"あと頑張れ":31,"あと 頑張れ":31,"赤 頑張れ":31,"赤 頑張ろう":31,"赤 まだいける":32,"赤 がんばろう":31,"あか まだいける":32,"袴田 行ける":32,"赤 いいね":33,"あか いいね":33,"赤いいね":33,"赤イエーイ":34,"あかいえーい":34,"アカ ありがとう":35,"アク ありがとう":35,"赤ありがとう":35,"みどり 頑張れ":41,"緑 頑張れ":41,"緑 頑張ろう":41,"みどり 頑張ろう":41,"みどり がんばろう":41,"緑 がんばろう":41,"緑 まだいける":42,"みどり まだいける":42,"緑 いいね":43,"みどり いいね":43,"緑イエーイ":44,"みどりイエーイ":44,"ミドリ ありがとう":45,"緑ありがとう":45,"黄色 頑張れ":51,"黄色 頑張ろう":51,"黄色 がんばろう":51,"黄色 まだいける":52,"きいろ まだいける":52,"黄色 いいね":53,"きいろ いいね":53,"黄色いいね":53,"黄色イエーイ":54,"きいろイエーイ":54,"黄色 ありがとう":55,"ヒーローありがとう":55,"紫 頑張ろう":61,"紫 頑張れ":61
,"紫 がんばろう":61,"紫 まだいける":62,"むらさき まだいける":62,"紫 いいね":63,"むらさき いいね":63,"紫イエーイ":64,"むらさきイエーイ":64,"紫 ありがとう":65,} #ストップ, 疲れた


while True:
    print(mic.list_microphone_names()[0]) #know the name of the mic used
    #print("User name A speak now")
    #with s_r.Microphone(sample_rate = 20000) as source:
    with mic as source:
        r.adjust_for_ambient_noise(source) #reduce noise
        #r.energy_threshold = 300 # minimum audio energy to consider for recording (300) 
        #r.dynamic_energy_threshold = False #ノイズレベルを自動に調整するかどうか。　
        #r.dynamic_energy_adjustment_damping = 0.15
        #r.operation_timeout = 0.3
        #r.phrase_threshold = 0.1 # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops) (0.3)
        #r.pause_threshold = 0.5 # seconds of non-speaking audio before a phrase is considered complete (0.8) 
        #r.non_speaking_duration = 0.1 # seconds of non-speaking audio to keep on both sides of the recording (0.5)
        startSeconds = timeit.default_timer()
        try:
            audio = r.listen(source, phrase_time_limit=2) # 1つの認識に制限時間を設けるのなら"timeout = 3"が目安 phrase_time_limit=3
            print("Now to recognize it...") 
            speech = r.recognize_google(audio, language='ja-JP')
            print(speech)
            print("--- 実行速度　%s  ---" %(timeit.default_timer() - startSeconds))
            #keyword_in_speech = [word for word in word_list if word in speech] #get if there are keywords
            keyword_in_speech = [word for word in word_list if word in speech]#get if there are keywords and its order
            #str_key_speech = " ".join(keyword_in_speech)
            #print(str_key_speech)
            print(keyword_in_speech)
            # websocket(keyword_in_speech)
            if keyword_in_speech != []:
                #for word[22] in keyword_in_speech:
                    #print(wordNumber_list[word[22]])
                for word in keyword_in_speech:
                    #送信
                    print(wordNumber_list[word])
                    websocket(wordNumber_list[word], "kishida")
                #     #thredを使ったバージョン
                #     #print(wordNumber_list[word], "Kisihida")
                #     #thread1 = threading.Thread(target=websocket, args=(wordNumber_list[word], "Kishida"))
                #     #thread1.start()
                #send_websocket("Kishida" + str_key_speech)

        except s_r.UnknownValueError:
            print("Could not understand audio")
        except s_r.RequestError as e:
            print("Could not request result from Google Speech Recognition service; {0}".format(e))
        except s_r.WaitTimeoutError:
            print("Timeout is over")




