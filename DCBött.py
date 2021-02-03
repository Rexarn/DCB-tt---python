import os
import asyncio

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord.abc import Messageable

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():  #Booting the bot..
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to a shit server:\n' #Tells us that it connected successfully
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members]) #Tells us which server it's on
    print(f'Names of the retards dumb enough to join:\n - {members}')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'pls nuke' in message.content.lower(): #activates the command
        await trigger_typing()
        msg = await message.channel.purge(limit=123)  #removes everything from the chat
        print(f"Target neutralized.") #console message
    
    if client.user.mentioned_in(message):  #if the bot is pinged, it will be pissed
        await trigger_typing()
        await message.channel.send("WHO THE FUCK PINGED ME?!") #As you can tell..
        await message.channel.send(file=discord.File(r'C:\Users\thomas.svensson9\source\repos\DCBött\DCBött\pinged.gif')) 
        #even throws a gif at us for good measure
                                                    #edit to your python launch directory..
        print(f"NO PING PLS") #console message


    if 'pls confess' in message.content.lower():
        await trigger_typing()
        await message.channel.send("..") 
        await message.channel.send(".....")
        await message.channel.send("No bots here, i swear :disappointed_relieved:") #They will never know :)
        print(f"Beep boop i won't confess") #CONSOOOOLE MESSAAAAGEEEEE


client.run(TOKEN)