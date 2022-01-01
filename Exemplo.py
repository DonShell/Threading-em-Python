import threading
import time
rodar = True
def Processo(variavel):

	while rodar:
		print("Processo " + variavel)
		time.sleep(0.5)


a = threading.Thread(target=Processo, args = ("A") )
b = threading.Thread(target=Processo, args = ("B") )

a.start()
b.start()

input("Pressione enter para encerrar!")
rodar = False
