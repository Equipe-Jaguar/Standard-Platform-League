try:
    import confNAO
    import qi
    import naoqi
    from naoqi import ALProxy, ALModule
except:
    print "Erro ao importar bibliotecas"

try:
	memoria = ALProxy('ALMemory', confNAO.ip_addr, 9559)
	movimento = ALProxy ('ALMotion', confNAO.ip_addr, 9559)
	print "Conectou ao NAO"
except:
	print "Nao conseguiu contato com o NAO"

def main():
    movimento.setStiffnesses("Head", 1.0)
    sentido = 1
    novoYaw=0
    while(1):
        temBola = memoria.getData("achouBola")
        yawAtual= movimento.getAngles('Head',True)
        #print (temBola[0])
        if (temBola[0]==True):
            #print("pos 1:" + str(temBola[1]))
            #print("pos 2:" + str(temBola[2]))
            #print(movimento.getAngles('HeadYaw',True))
            ajustefino = 120 - temBola[1]
            novoYaw=yawAtual[0]
            #novoYaw = yawAtual[0] + 0.00001*ajustefino
            print (ajustefino)
        else:
            novoYaw = yawAtual[0] + (0.05*sentido)

        movimento.setAngles('HeadYaw', novoYaw, 0.2)

        if (novoYaw< -1.1 or novoYaw >1.1):
            sentido = sentido*(-1)
            #break
    #time.sleep (1000)
    movimento.setStiffnesses("Head", 0.0)
    print ("Saiu")

if __name__ == "__main__":
    main()
