import discord
import reply

bot_token = "" # Discord Bot Token

# Discord
client = discord.Client()

@client.event
async def on_ready():
	print("Logged in as", client.user.name, client.user.id)

@client.event
async def on_message(message):
	if ((message.type == discord.MessageType.default) and (client.user != message.author)):
		text = message.content
		print(message.author.name)
		res = reply.make_reply(text)
		channel = message.channel
		async with channel.typing():
			await channel.send(res)

client.run(bot_token)
