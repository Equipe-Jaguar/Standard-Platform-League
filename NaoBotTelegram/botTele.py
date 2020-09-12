import telepot 
from pprint import pprint
#import naoqi

bot = telepot.Bot("1145928454:AAEbA27PC9wE82OM0N8bFg8pUE9WCf3fz84")
msg_antigas = []

while True:

    # RECEBE AS MENSAGENS
    mensagens = bot.getUpdates()[-1]
    #pprint(mensagens)

    # SE EXISTIR NOVA MENSAGEM
    if mensagens:
        remente_name = mensagens['message']['chat']['first_name']
        remetente_id = mensagens['message']['chat']['id']
        remetente_user = mensagens['message']['chat']['username']

        msg_id = mensagens['message']['message_id']
        msg = mensagens['message']['text']

        if msg_id not in msg_antigas:
            msg_antigas.append(msg_id)

            print(msg_id)
            print(">>> Mensagem de: %s"%(remetente_user))


            if msg == "/start":
                bot.sendMessage(remetente_id, "Ola! Eu sou a Pablo, jogadora de futebol da Equipe Jaguar! Muito prazer em te conhecer. O que gostaria que eu fizesse? ")
                bot.sendMessage(remetente_id, ">>> digite /ola para que eu diga um Ola especialmente para voce")
                bot.sendMessage(remetente_id, ">>> digite /chute para que eu execute um chute forte")
                bot.sendMessage(remetente_id, ">>> digite /danceOnda para que eu dance Olha a Onda")

            elif msg == "/ola":
                bot.sendMessage(remetente_id, "OK, vou te dar um oi!")
                #NAOQI ENTRA AQUI

            elif msg == "/chute":
                bot.sendMessage(remetente_id, "OK, vou chutar!")
                #NAOQI ENTRA AQUI

            elif msg == "/danceOnda":
                bot.sendMessage(remetente_id, "OK, vou dancar a coreografia da musica Olha a Onda.")
                #NAOQI ENTRA AQUI
            
            else:
                bot.sendMessage(remetente_id, "Comando inexistente.")

        



