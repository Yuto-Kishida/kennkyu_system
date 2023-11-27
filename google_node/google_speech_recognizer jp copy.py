#Synchronous Recognition, limited to a minute or Less
#480 hours of audio per day
#900 requests per 60 seconds
#https://cloud.google.com/speech-to-text/quotas
from operator import truediv
import speech_recognition as s_r
import pyaudio
import json
from websocket import create_connection
import socket
import time
import timeit

start_time = time.time()
json_data = {
    "user":{"name":"","data":1}
}

#HOST = '127.0.0.1'   # juliusサーバーのIPアドレス
#PORT = 10500         #juliusサーバーの待ち受けポート
#DATESIZE = 1024     # 受信データバイト数
#json_data = {
#    "user":{"name":"","data":1}
#}

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

word_list = ["rápido", "rápida", "lento", "todavía puedo", "cansado",
             "cansada", "lo pude hacer", "difícil", "イエーイ", "si", "no"]
wordNumber_list = {"rápido": 0, "rápida": 0, "lento": 1, "lenta": 1, "todavía puedo": 2, "cansado": 3,
                    "cansada": 3, "lo pude hacer": 4, "difícil": 5, "イエーイ": 6, "si": 8, "no": 9}

while True:
    #print(mic.list_microphone_names()[0]) #know the name of the mic used
    print("Speak now")
    #with s_r.Microphone(sample_rate = 20000) as source:
    with mic as source:
        r.adjust_for_ambient_noise(source) #reduce noise
        r.energy_threshold = 300 # minimum audio energy to consider for recording (300) 
        r.dynamic_energy_threshold = False #ノイズレベルを自動に調整するかどうか。　
        #r.dynamic_energy_adjustment_damping = 0.15
        #r.operation_timeout = 0.5
        r.phrase_threshold = 0.1 # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops) (0.3)
        #r.pause_threshold = 0.5 # seconds of non-speaking audio before a phrase is considered complete (0.8) 
        #r.non_speaking_duration = 0.1 # seconds of non-speaking audio to keep on both sides of the recording (0.5)
        startSeconds = timeit.default_timer()
        try:
            audio = r.listen(source, phrase_time_limit=3, timeout = 3) # 1つの認識に制限時間を設けるのなら"timeout = 3"が目安 phrase_time_limit=3
            print("Now to recognize it...") 
            speech = r.recognize_google(audio, language='es-MX')
            print(speech)
            print("--- 実行速度　%s  ---" %(timeit.default_timer() - startSeconds))
            #keyword_in_speech = [word for word in word_list if word in speech] #get if there are keywords
            keyword_in_speech = [word for word in word_list if word in speech.lower()]#get if there are keywords and its order
            print(keyword_in_speech)
            if keyword_in_speech != []:
                for word in keyword_in_speech:
                    #送信
                    print(wordNumber_list[word])
                    websocket(wordNumber_list[word], "Kishida")

        except s_r.UnknownValueError:
            print("Could not understand audio")
        except s_r.RequestError as e:
            print("Could not request result from Google Speech Recognition service; {0}".format(e))
        except s_r.WaitTimeoutError:
            print("Timeout is over")



