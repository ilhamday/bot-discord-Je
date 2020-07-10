import discord
import joke_api

client = discord.Client()

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
            await message.channel.send('Jokenya ngga dapet. Coba lagi nanti.')
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])


client.run('NzMxMDMwMjk5MTYwNjA4Nzcw.XwgLUg.Ma_EU911y4mnU5pL4_YLrnyqVKQ')