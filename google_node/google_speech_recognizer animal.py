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
import threading

start_time = time.time()
json_list = {
    "key" : [] 
}
json_data = {
    "user":{"name":"","data":""}
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
word_list = ["よろしく","早い", "遅い","まだいける","疲れた","うまくできた","難しい","イエーイ","ふぅー","イエス","YES","yes","ノー","NO","No","ニュース","はい", "YEAH","の","いいね","頑張ろう","いいえ","家","A","まだ行ける","頑張れ","みんな頑張れ","みんながんばれ","みんながんばろう","がんばれみんな","みんな頑張ろう","頑張ろうみんな","がんばろうみんな","みんなまだいける","まだいけるみんな","みんないいね","いいねみんな","みんなイエーイ","イエーイみんな","みんなうまくできた","パンダ 頑張れ","パンダ がんばろ","パンダ 頑張ろう","パンダ がんばれ","パンダ まだいける","パンダ いいね","パンダいね","パンダ イエーイ","パンダ いえーい","狐 頑張ろう","キツネ 頑張ろう","赤 まだいける","あか まだいける","赤 いいね","あか いいね","赤イエーイ","あかいえーい","みどり 頑張れ","緑 頑張れ","緑 頑張ろう","みどり 頑張ろう","みどり がんばろう","緑 がんばろう","緑 まだいける","みどり まだいける","緑 いいね","みどり いいね","緑イエーイ","みどりイエーイ","黄色 頑張ろう","黄色 がんばろう","黄色 まだいける","きいろ まだいける","黄色 いいね","きいろ いいね","黄色イエーイ","きいろイエーイ","紫 頑張ろう","紫 がんばろう""紫 まだいける","むらさき まだいける","紫 いいね","むらさき いいね","紫イエーイ","むらさきイエーイ",] #ストップ, 疲れた
wordNumber_list = {"早い":0, "遅い":1,"まだいける":2,"まだ行ける":2,"疲れた":3,"うまくできた":4,"難しい":5,"イエーイ":6,"よろしく":9,"YEAH":6,"Yeah":6,"イエス":15,"ノー":16,"YES":15,"NO":16,"No":16,"いいえ":16,"家":16,"yes":15,"ニュース":15,"はい":15,"の":16,"いいね":7,"頑張ろう":8,"頑張れ":8,"みんながんばれ":10,"みんな頑張れ":10,"みんながんばろう":10,"がんばれみんな":10,"みんな頑張ろう":10,"頑張ろうみんな":10,"がんばろうみんな":10,"みんなまだいける":11,"まだいけるみんな":11,"みんないいね":12,"いいねみんな":12,"みんなイエーイ":13,"イエーイみんな":13,"みんなうまくできた":14,"パンダ がんばれ":21,"パンダ がんばろ":21,"パンダ　頑張ろう":21,"パンダ がんばれ":21,"パンダ まだいける":22,"パンダ いいね":23,"パンダいね":23,"パンダ イエーイ":24,"パンダ いえーい":24,"あと頑張れ":31,"あと 頑張れ":31,"赤 頑張れ":31,"赤 頑張ろう":31,"赤 まだいける":32,"赤 がんばろう":31,"あか まだいける":32,"赤 いいね":33,"あか いいね":33,"赤イエーイ":34,"あかいえーい":34,"みどり 頑張れ":41,"緑 頑張れ":41,"緑 頑張ろう":41,"みどり 頑張ろう":41,"みどり がんばろう":41,"緑 がんばろう":41,"緑 まだいける":42,"みどり まだいける":42,"緑 いいね":43,"みどり いいね":43,"緑イエーイ":44,"みどりイエーイ":44,"黄色 頑張ろう":51,"黄色 がんばろう":51,"黄色 まだいける":52,"きいろ まだいける":52,"黄色 いいね":53,"きいろ いいね":53,"黄色イエーイ":54,"きいろイエーイ":54,"紫 頑張ろう":61,"紫 がんばろう":61,"紫 まだいける":62,"むらさき まだいける":62,"紫 いいね":63,"むらさき いいね":63,"紫イエーイ":64,"むらさきイエーイ":64,} #ストップ, 疲れた


while True:
    print(mic.list_microphone_names()[0]) #know the name of the mic used
    print("User name A speak now")
    #with s_r.Microphone(sample_rate = 20000) as source:
    with mic as source:
        r.adjust_for_ambient_noise(source) #reduce noise
        #r.energy_threshold = 300 # minimum audio energy to consider for recording (300) 
        #r.dynamic_energy_threshold = False #ノイズレベルを自動に調整するかどうか。　
        #r.dynamic_energy_adjustment_damping = 0.15
        #r.operation_timeout = 0.5
        #r.phrase_threshold = 0.1 # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops) (0.3)
        #r.pause_threshold = 0.5 # seconds of non-speaking audio before a phrase is considered complete (0.8) 
        #r.non_speaking_duration = 0.1 # seconds of non-speaking audio to keep on both sides of the recording (0.5)
        startSeconds = timeit.default_timer()
        try:
            audio = r.listen(source, phrase_time_limit=2, timeout = 3) # 1つの認識に制限時間を設けるのなら"timeout = 3"が目安 phrase_time_limit=3
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
                     websocket(wordNumber_list[word], "Kishida")
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




