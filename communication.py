#TODO: Look at making 1 single connection that does not reset every time that the loop goes through

import qi
from socket import *
from construct import Container, ConstError
from gamestate import GameState, RobotInfo, ReturnData, GAME_CONTROLLER_RESPONSE_VERSION
#import logging
#import unboard
import confNAO
from naoqi import ALProxy, ALModule

leds = ALProxy('ALLeds', confNAO.ip_addr, 9559)
memoria = ALProxy('ALMemory', confNAO.ip_addr, 9559)
#leds.off('AllLeds')

#session para poder se inscrever
session = qi.Session()

#portas do game controller
GAME_CONTROLLER_LISTEN_PORT = 3838
GAME_CONTROLLER_ANSWER_PORT = 3939


def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    try:
        #tenta bindar no endereco de broadcast da rede, muda de acordo com as
        #configuracoes dela. Se o programa nao for matado corretamente (
        #ex. dar ctrl+c em vez de ctrl+\), nao vai dar pra bindar nessa porta,
        #pois ela ja vai estar ocupada
        #leds.off('LeftFaceLeds')
        leds.off('LeftFaceLeds')
    	leds.on('LeftFaceLedsGreen')
        #leds.on('LefFootLedsGreen')
        udpSocket.bind((confNAO.ip_gm, GAME_CONTROLLER_LISTEN_PORT))
        print("Conectou!!!")
    except Exception as identifier:
        print("Bind error")
        #leds.off('LeftFaceLeds')
        leds.on('LeftFaceLedsRed')
        #leds.on('LeftFootLedsRed')
        #if (identifier.erro == 98):  #addr already in use
        #    return
    try:
        while (1):
            #tenta catar pacotes com o tamanho setado no game controller
            data, peer = udpSocket.recvfrom(GameState.sizeof())

            #logging.debug(len(data))

            #transforma dos dados puros que foram recebidos na porta para a "struct" de python.
            parsed_state = GameState.parse(data)

            #Checagem para a troca de lado ao trocar o tempo
            if(int(parsed_state.teams[0].team_number) == confNAO.team_number):
                teamNumber = 0
            else:
                teamNumber = 1

            # logging.debug("packet from broadcast is :" + peer[0])
            # for structKey, structValue in thisState.iteritems():
            #     logging.info("key: {} in struct recieved is {}".format(
            #         structKey, structValue))

            #loggando alguns dados para saber se esta recebendo o pacote corretamente
            #print("gamephase : {}".format(parsed_state.gamePhase))
            #print("game_state : {}".format(parsed_state.game_state))
            memoria.insertData("gamestate",parsed_state.game_state)
            #print("first_half : {}".format(parsed_state.first_half))
            #print("secsRemaining : {}".format(parsed_state.secsRemaining))
            memoria.insertData("secsRemaining",parsed_state.secsRemaining)
            #print("penalty : {}".format(parsed_state.teams[teamNumber].players[confNAO.player_number].penalty))
            memoria.insertData("penalty",parsed_state.teams[teamNumber].players[confNAO.player_number].penalty)
            #print("pickup : {}".format(parsed_state.teams[teamNumber].players[confNAO.player_number].pick_up))

            if parsed_state.game_state == "STATE_FINISHED":
                leds.off('LeftFaceLeds')
                leds.on('LeftFaceLedsRed')
                break

            #update unboard
            #print(parsed_state.game_state)
            # print("1", unboard.gameState)
            #print( parsed_state.teams[teamNumber].players[confNAO.player_number].penalty)

            #dados de retorn para o GC
            data = Container(
                header=b"RGrt",
                version=GAME_CONTROLLER_RESPONSE_VERSION,
                team=confNAO.team_number,#50,  #UnBeatables number
                player=confNAO.player_number, #1,
                message=0)

            try:
                destination = peer[0], GAME_CONTROLLER_ANSWER_PORT
                udpSocket.sendto(ReturnData.build(data), destination)
            except Exception as e:
                print("Network Error: %s" % str(e))
    finally:
        #fecha a conexao se o codigo sair do while para poder ser reaberta dps
        try:
            udpSocket.shutdown(SHUT_RDWR)
        except Exception as ex:
            print("could not shutdown")
        udpSocket.close()

if __name__ == '__main__':
    main()
