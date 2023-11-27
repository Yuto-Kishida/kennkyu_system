import speech_recognition as s_r
import pyaudio
import timeit
print(pyaudio.__file__)
print(s_r.__version__)
r = s_r.Recognizer()
mic = s_r.Microphone()
#word_list = ["早い", "遅い","まだいける","疲れた","うまくできた","難しい","イエーイ","ふぅー","イエス","YES","ノー","NO","No"]
#wordNumber_list = {"早い":0, "遅い":1,"まだいける":2,"疲れた":3,"うまくできた":4,"難しい":5,"イエーイ":6,"ふぅー":7,"イエス":8,"ノー":9,"YES":8,"NO":9,"No":9}
word_list = ["rápido", "rápida", "lento", "todavía puedo", "cansado",
             "cansada", "lo pude hacer", "difícil", "イエーイ", "si", "no"]
wordNumber_list = {"rápido": 0, "rápida": 0, "lento": 1, "lenta": 1, "todavía puedo": 2, "cansado": 3,
                    "cansada": 3, "lo pude hacer": 4, "difícil": 5, "イエーイ": 6, "si": 8, "no": 9}
with mic as source:
    r.adjust_for_ambient_noise(source)
    while True:
        print("Habla por favor")
        startSeconds = timeit.default_timer()
        try:
            audio = r.listen(source, phrase_time_limit=3) #take voice input from the microphone
            print("--- %s segundos listen ---" % (timeit.default_timer() - startSeconds))
            startSeconds = timeit.default_timer()
            print("Ahora a reconocerla...")
            speech = r.recognize_google(audio, language='es-MX')
            print(speech)
            print("--- %s segundos recognize_google---" % (timeit.default_timer() - startSeconds))
            keyword_in_speech = [word for word in word_list if word in speech.lower()]#get if there are keywords and its order
            print(keyword_in_speech)
            if keyword_in_speech != []:
                for word in keyword_in_speech:
                    #送信
                    print(wordNumber_list[word])
        except s_r.UnknownValueError:
            print("No se pudo entender el audio")
            print("--- %s segundos ---" % (timeit.default_timer() - startSeconds))
        except s_r.RequestError as e:
            print("No se pudo obtener un resultado de la solicitud al servico de Google Speech Recognition; {0}".format(e))
            print("--- %s segundos ---" % (timeit.default_timer() - startSeconds))
        except s_r.WaitTimeoutError:
            print("Tu tiempo se terminó")
            print("--- %s segundos ---" % (timeit.default_timer() - startSeconds))