import threading
import time
import random

numUsuarios = 5  
numMings = 8;     
esquemaMings = ['-', '-', '-', '-', '-', '-', '-', '-'] 

mings = [threading.Semaphore(1) for i in range(numMings)] 

def mostrarEsquema(mings): 
    print("[", end = "")
    for i in range(0,8):
         print(mings[i], end = "") 
    print("]")

def desbloqueaLugar(cual): 
    mings[cual].release()

def bloqueaLugar(cual): 
    mings[cual].acquire()

def desocupaLugar(quien, cual):
    mings[cual].release() 
    dice(quien, '¡Que alivio! Desocupo el mingitorio %d' % cual)
    esquemaMings[cual] = '-' 
    mostrarEsquema(esquemaMings)
    
    desbloqueaLugar(cual+1)

def ocupaLugar(quien, cual):
    mings[cual].acquire() 

    dice(quien, 'Ocupo el mingitorio %d' % cual)
    esquemaMings[cual] = 'X' 
    mostrarEsquema(esquemaMings)
    time.sleep(random.randint(0,3)) 
    desocupaLugar(quien, cual) 

def dice(quien, msg):
    print('[%d] - %s' % (quien, msg))

def busca(quien):
    dice(quien, 'Buscando...')
    cual = random.randint(0,7)
    ocupaLugar(quien, cual) 

def entra(quien): 
    dice(quien, '¡Tengo ganas!')
    busca(quien)

def usuario(quien):
    dice(quien, 'Existo')

    while True: 
        entra(quien)

usuarios = [threading.Thread(target=usuario, args=[i]) for i in range(numUsuarios)]
for i in usuarios:
    i.start() 