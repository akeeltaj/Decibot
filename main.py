
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
  user = discord.user
  
  
                               
  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)
  if message.author == client.user:
    return
  if message.content.startswith('$test'):
    await message.channel.send('I\'m alive')
  
  if message.content.startswith('$version'):
    await message.channel.send(discord.version_info)
  username = message.author.name
  created = message.author.created_at
  userid = message.author.id
  dmchannel = message.author.dm_channel
  try:  
    if message.content.startswith('$userdata'):
      await message.channel.send(f'User {username} was created on {created}. The unique ID is {userid}. DM channel value is {dmchannel} '  )
  except Exception as e:
      await message.channel.send(e)


#print(discord.user.display_name)
  
client.run(TOKEN)