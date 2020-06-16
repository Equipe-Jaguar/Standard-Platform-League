#importando as bibliotecas necessarias
try:
	import confNAO
	import qi
	import naoqi
	import numpy as np
	import cv2
	from naoqi import ALProxy, ALModule
except:
	print "Erro ao importar bibliotecas"

#conecatao aos proxys do robo
try:
	memoria = ALProxy('ALMemory', confNAO.ip_addr, 9559)
	leds = ALProxy('ALLeds', confNAO.ip_addr, 9559)
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
def procuraBola(numcam):
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
		#print (balls)
		encontrados = False

		if (len(balls)>0):
			encontrados = True
			#posicoes = balls[0]
			#print ("valor 0 " + str(balls[0]))
			#print ("valor 1 " + str(balls[0][0])
			#print ("Valor 2 " + str(balls[0][1]))
			leds.off('LeftFaceLedsRed')
			leds.on('LeftFaceLedsGreen')

	if (encontrados == True):
		return(True,balls[0][0],balls[0][1])
	else:
		return(False,0,0)


def main(): #Funcao principal
	camera = 0;
	while (1):
		achou = procuraBola(camera)
		#print (achou[0])
		#print (camera)
		memoria.insertData("achouBola",achou)
		if (achou[0]==False):
			leds.off('RightFaceLeds')
			leds.on('RightFaceLedsRed')
			if (camera == 0):
				camera = 1
			else :
				camera = 0
		else:
			leds.off('RightFaceLeds')
			leds.on('RightFaceLedsGreen')

if __name__ == "__main__":
    main()
