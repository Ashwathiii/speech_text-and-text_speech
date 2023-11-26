import pyttsx3

txt_sp = pyttsx3.init()
txt = input("Enter the text to convert...\n")
txt_sp.say(txt)
txt_sp.runAndWait()
