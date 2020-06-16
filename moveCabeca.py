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
    cont = 1
    while(1):
        temBola = memoria.getData("achouBola")
        #print (temBola[0])
        if (temBola[0]==True):
            #print("pos 1:" + str(temBola[1]))
            #print("pos 2:" + str(temBola[2]))
            print(movimento.getAngles('HeadYaw',True))
            cont = cont + 1
        else:
            yawAtual= movimento.getAngles('Head',True)
            novoYaw = yawAtual[0] + 0.05
            movimento.setAngles('HeadYaw', novoYaw, 0.2)


        if (cont==25):
            break
    #time.sleep (1000)
    movimento.setStiffnesses("Head", 0.0)
    print ("Saiu")

if __name__ == "__main__":
    main()
