#importando as bibliotecas necessarias
try:
	import confNAO
	import qi
	import naoqi
	import numpy as np
	import cv2
	#import descanso
	#import chutefort
	#import chutedir
	#import cascadebaixo
	#import cabecabaixa
	#import cabeca
	from naoqi import ALProxy, ALModule
except:
	print "Erro ao importar bibliotecas"

#conecatao aos proxys do robo
try:
	posture = ALProxy('ALRobotPosture', confNAO.ip_addr, 9559)
	memoria = ALProxy('ALMemory', confNAO.ip_addr, 9559)
	leds = ALProxy('ALLeds', confNAO.ip_addr, 9559)
	movimento = ALProxy ('ALMotion', confNAO.ip_addr, 9559)
	print "Conectou ao NAO"
except:
	print "Nao conseguiu contato com o NAO"

#Conectando na cam do robo
while True:
	try:
    	videoDevice = ALProxy('ALVideoDevice', confNAO.ip_addr, 9559)
		print "Conectou no video"
		break
	except:
		print 'erro video, vamos tentar de novo'
		#videoDevice=ALProxy('ALVideoDevice',confNAO.ip_addr,9559)
		handles = videoDevice.getSubscribers()
		for cam in handles:
        		videoDevice.unsubscribe(cam)


#para o robo assumir a postura agachado
#movimento.setStiffnesses("Body", 1.0)
#posture.goToPosture('Crouch',0.8)
#movimento.setStiffnesses("Body", 0.0)
#leds.off('AllLeds')

#subscribe top camera
AL_kTopCamera = 0	#Define a camera superior
AL_kDownCamera = 1	#Define a camera inferior
AL_kQVGA = 1            #Define resolucao 320x240
AL_kBGRColorSpace = 13  #Define padrao BGR de cor
captureTopDevice = videoDevice.subscribeCamera("cima", AL_kTopCamera, AL_kQVGA, AL_kBGRColorSpace, 10)
captureDownDevice = videoDevice.subscribeCamera("baixo", AL_kDownCamera, AL_kQVGA, AL_kBGRColorSpace,10)
#Def captureDevice como modulo test, camera superior, resolucao, cor, FPS

# criando uma imagem em branco
width = 320
height = 240
image = np.zeros((height, width, 3), np.uint8)
saida = np.zeros((height, width, 1), np.uint8)

#definindo caminho do arquivo da rede neural
ball_cascade = cv2.CascadeClassifier('ball.xml')

#ROTINA do Cascade
def procurabola(numcam):
	leds.off('LeftFaceLeds')
	leds.on('LeftFaceLedsRed')
	if (numcam>0):
		result = videoDevice.getImageRemote(captureDownDevice)
	else:
		result = videoDevice.getImageRemote(captureTopDevice)

    	#analizando a imagem capturadas
	if result == None:
		print ('cannot capture.')
		handles = videoDevice.getSubscribers()
                for cam in handles:
                        videoDevice.unsubscribe(cam)
		encontrados = False
		#videoDevice = ALProxy('ALVideoDevice', confNAO.ip_addr, 9559)
	else:
		values = map(ord, list(result[6]))
		i = 0
		for y in range(0, height):
			for x in range(0, width):
				image.itemset((y, x, 0), values[i + 0])
				image.itemset((y, x, 1), values[i + 1])
				image.itemset((y, x, 2), values[i + 2])
				i += 3

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		balls = ball_cascade.detectMultiScale(gray, 1.6, 2)

		encontrados = False

		if (len(balls)>0):
			encontrados = True
			leds.off('LeftFaceLedsRed')
			leds.on('LeftFaceLedsGreen')

	if (encontrados == True):
		return(True,balls[0][0],balls[0][1])
	else:
		return(False,0,0)


def alinha0(posx,posy):
	#xbola
        if (posx) <= 40:
		print "esquerda1"
                alinhalado.cm(0.2)
	elif ((80 >= posx) and (posx > 40)):
                print "esquerda2"
                alinhalado.cm(0.1)
	elif ((140 >= posx) and (posx > 80)):
                print "centro"
                #setdistpasso1.cm(0.15)
                alinhalado.cm(-0.036)
     	elif ((200 >=posx) and (posx > 140)):
                print "direita2"
        	alinhalado.cm(-0.1)
     	elif ((240>=posx) and (posx > 200)):
             	print "direita1"
                alinhalado.cm(-0.2)

        #ybola7
    	if (200 >= posy):
          	print "longe"
                setdistpasso1.cm(1)
       	else:
                print "longissimo"
                setdistpasso1.cm(0.7)
                #chutefort.do()

def alinha1(posx,posy):
	print (posy)
        #xbola
	if (posx) <= 40:
                print "esquerda1"
                alinhalado.cm(0.2)
        elif ((80 >= posx) and (posx > 40)):
                print "esquerda2"
                alinhalado.cm(0.1)
        elif ((140 >= posx) and (posx > 80)):
                print "centro"
                #setdistpasso1.cm(0.15)
                alinhalado.cm(-0.033)
        elif ((200 >=posx) and (posx > 140)):
                print "direita2"
                alinhalado.cm(-0.1)
        elif ((240>=posx) and (posx > 200)):
                print "direita1"
                alinhalado.cm(-0.2)

        #ybola
	if (25 >= posy):
                print "6"
                setdistpasso1.cm(0.65)
        elif (45 >=posy) and (posy > 25):
                print "5"
                setdistpasso1.cm(0.555)
                #chutefort.do()
        elif (60 >= posy) and (posy > 45):
                print "4"
                setdistpasso1.cm(0.45)
                #chutefort.do()
	elif (95 >=posy) and (posy > 60):
                print "3"
                setdistpasso1.cm(0.35)
                #chutefort.do()
        elif (160 > posy) and (posy > 95):
                print "2"
                setdistpasso1.cm(0.24)
                #chutefort.do()
        elif (posy >= 160):
                print "1"
                setdistpasso1.cm(0.11)
                #chutefort.do()

def alinhabaixo(posx,posy):
	print (posy)
	if (posy < 70):
		descanso.do(1)
        	if (posx) <= 40:
                   	print 'ajustando e1'
                        alinhalado.cm(0.05)
                        setdistpasso1.cm(0.04)
           	elif (80 >= posx) and (posx > 40):
                    	print 'ajustando e2'
                        alinhalado.cm(0.02)
                 	setdistpasso1.cm(0.04)
             	elif (160 >= posx) and (posx > 80):
                        print 'ajustando c'
                        setdistpasso1.cm(0.045)
                elif (200 >= posx) and (posx > 160):
                        print 'ajustando d2'
                        alinhalado.cm(-0.02)
                        setdistpasso1.cm(0.04)
             	elif (240 >= posx) and (posx> 200):
                        print 'ajustando d1'
                        alinhalado.cm(-0.046)
                     	setdistpasso1.cm(0.04)
               	else:
                	print 'n al'
      	else:
		#descanso.do(1)
        	#xbola
		movimento.setStiffnesses("Body", 1.0)
		if posx <= 40:
                	print "esquerda1"
                        alinhalado.cm(0.046)
                        chutefort.do()
              	elif (90 >= posx) and (posx > 40):
                     	print "esquerda2"
                        #alinhalado.cm(0.04)
                        chutefort.do()
              	elif (125 >=posx) and (posx > 90):
                         print "centro"
			 #setdistpasso1.cm(-0.005)
                         alinhalado.cm(-0.05)
                         chutefort.do()
              	elif (220 >=posx) and (posx > 125):
                         print "direita2"
                         #alinhalado.cm(-0.03)
                         chutedir.do()
               	elif (240 >=posx) and (posx > 220):
                         print "direita1"
                         alinhalado.cm(-0.046)
                         chutedir.do()
               	else:
                         print "nao achou"
                         alinhalado.cm(-0.046)


'''
while True:
	i=1
	q=1



    
	while True:
		if i>1:
			break
		print 'Inicia'
                posture.goToPosture('StandInit',0.5)
		#descanso.do(1)
                achou = procurabola(0)
                if achou[0]==True:
                        print "Achou em cima"
			alinha0(achou[1],achou[2])
			break
                achou = procurabola(1)
                if achou[0] ==True:
                        print "Achou em baixo"
			alinha1(achou[1],achou[2])
			cabecabaixa.do()
			achou = procurabola(1)
			if achou[0]==True:
				alinhabaixo(achou[1],achou[2])
		cabecabaixa.do()
		achou = procurabola(1)
		if achou[0]==True:
			alinhabaixo(achou[1],achou[2])
		i=i+1

	print 'saiu'
	if achou[0] == False:
		while True:
			descanso.do(1)
			cabeca.do(2)
			#bracotras.do()
			achou = procurabola(0)
			if achou[0] == True:
				if achou[1] <= 100:
					alinhalado.cm(0.3)
				elif (achou[1]>100) and (achou[1]<=200):
					alinhalado.cm(0.25)
				elif achou[1] > 200:
					alinhalado.cm(0.15)
				#movimento.moveTo(0,0,0.785)
				break
			achou = procurabola(1)
			movimento.setStiffnesses("Body", 1.0)
			if achou[0] == True:
				alinhalado.cm(0.35)
				#movimento.moveTo(0,0-0.785)
				break
			descanso.do(1)
			cabeca.do(5)
			#bracotras.do()
			achou = procurabola(0)
			movimento.setStiffnesses("Body", 1.0)
        		if achou[0] == True:
		        	if achou[1] <= 100:
                                	alinhalado.cm(-0.3)
                                elif (achou[1] > 10) and (achou[1] <= 200):
                                	alinhalado.cm(-0.25)
                                elif achou[1] > 200:
                                	alinhalado.cm(-0.15)
                                 #movimento.moveTo(0,0,-0.785)
                             	break
        		achou =	procurabola(1)
        		if achou[0] == True:
                	 	alinhalado.cm(-0.35)
				#movimento.moveTo(0,0-0.785)
			q = q+1
			if q>2:
                		setdistpasso1.cm(0.3)
			else:
				print 'continua'
			break
            '''


	#chutefort.do()
