import speech_recognition as sr
def speech_recog():
    r=sr.Recognizer()   #r is obj for recognizer
    mic=sr.Microphone()  #mic is obj for microphone class
    while True :  #repeat ayt paryn
        with mic as source:
            print("speak.............")
            audio=r.listen(source)



            try:
                text=r.recognize_google(audio)
                print("you said.......",text)
            except sr.UnknownValueError:        #onnum detect ayyllenk
                print("didnt hear anything please repeat..........")
speech_recog()