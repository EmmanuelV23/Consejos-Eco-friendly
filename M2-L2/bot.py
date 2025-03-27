import discord
# import * - es una forma rápida de importar todos los archivos de la biblioteca
from main import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


# Una vez que el bot esté listo, ¡imprimirá su nombre!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('?eco'):
        await message.channel.send(gen_advice())
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")


client.run("TOKEN")