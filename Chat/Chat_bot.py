from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chat = ChatBot('Eva')
talk = ['Hola Eva','¿Que tal?','Tengo una pregunta',
        'Si,dime','¿Como esta el clima?','Hace frio y hay sol',
        '¿Hay viento?','No,no hay viento','Gracias','Merece',
        'Adios','Nos vemos Sebastian','¿Conoces a mi esposa?'
        ,'Si se llama Lucia']

trainer = ListTrainer(chat)
trainer.train(talk)

while True:
    peticion = input('Tu: ')
    respuesta = chat.get_response(peticion)

    print('Eva: ',respuesta)

