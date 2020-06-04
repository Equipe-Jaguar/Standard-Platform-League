import qi
import confNAO
from naoqi import ALProxy, ALModule

memoria = ALProxy('ALMemory', confNAO.ip_addr, 9559)

def main():
    old_valor = "a"
    valor = "a"
    old_penalty = "a"
    penalty = "a"
    while True:
        valor = memoria.getData("gamestate")
        penalty = memoria.getData("penalty")
        if valor == "STATE_FINISHED":
            break
        if old_valor != valor:
            old_valor = valor
            print ("GameState:" + valor)

        if old_penalty != penalty:
            old_penalty = penalty
            print ("Penalty:" + str(penalty))

if __name__ == '__main__':
    main()
