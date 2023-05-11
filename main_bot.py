import discord
from bot_logic import gen_pass
from bot_logic import roll_dice
from bot_logic import guess_number
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('gen_pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('roll'):
        await message.channel.send(roll_dice())
    elif message.content.startswith('guess my number'):
        await message.channel.send(guess_number())

client.run("#Your bot code here")
