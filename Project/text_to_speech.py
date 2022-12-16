from gtts import gTTS
import os

abc = open('sample01.txt')
t = abc.read()


l = 'en'
obj = gTTS(text=t, lang=l, slow=False)
obj.save('sample01.mp3')