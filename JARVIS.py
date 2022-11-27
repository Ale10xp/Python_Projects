import alexandre_lib as bell
import re
#import vlc

#p = vlc.MediaPlayer("C:\\Users\Alexandre\Desktop\Bem vindo Sessão Gaming.mp3")
 
#p.play()


comand = input("Input the comand [cursos, games, lofi, chat, draw, python, \n strategy, watch, english, unity: ")
comand = comand.lower()
comand = re.sub(" ", "", comand)


comands = comand.split(",")

for i in range(len(comands)):
    bell.setup(str(comands[i]))

