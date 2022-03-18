
import os
import discord
import requests
import json


TOKEN = os.environ['DiscordKey']
client = discord.Client()


def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_random = json.loads(response.text)
  quote = json_random[0]['q'] + ' -' + json_random[0]['a'] 
  return(quote)

@client.event
async def on_ready():
  print('INFO: logged in as {0.user}'.format(client) )

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(TOKEN)