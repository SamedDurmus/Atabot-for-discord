



import discord
import nest_asyncio 
nest_asyncio.apply()
import requests 
import json
from discord.ext import commands
from utils import *
from functions import *


client = discord.Client()
intents = discord.Intents(messages = True, guilds= True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!',intents=intents)


@client.event
async def on_member_join(member):  
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"{member} aramıza katıldı. Hoş geldi!")

@client.event
async def on_member_remove(member):
      channel = discord.utils.get(member.guild.text_channels,name="genel")
      await channel.send(f"{member} siktirip gitti")

@client.event
async def on_command_error(ctx,error):
    await ctx.send(error)


@client.command()
async def clear(ctx, amount: int):
     await ctx.channel.purge(limit=amount)
    
    
def get_quote():
    response = requests.get("https://ataturk.vercel.app/tr")
    json_data = json.loads(response.text)
    quote= json_data["quote"]
    return (quote)

@client.event
async def on_ready():
    print("AtaBot {0.user} giris yapti.".format(client))
    
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith("!atatürk"):
        q = get_quote()
        await message.channel.send(q)

                

client.run("YOUR DISCORD BOT TOKEN")


        
    
    
    

