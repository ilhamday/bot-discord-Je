import discord
import joke_api
from mytoken import my_token

client = discord.Client()
my_token = my_token

@client.event
async def on_ready():
    print(f'We have looged in as {format(client)}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$joke'):
        joke = joke_api.get_joke()

        if joke == False:
            await message.channel.send('Sorry, no jokes for now~')
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])


client.run(my_token)