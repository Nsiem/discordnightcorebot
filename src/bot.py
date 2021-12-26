import os
from sys import executable
from time import sleep
import discord
from discord import voice_client
from discord.ext import commands
from dotenv import load_dotenv
import youtubesearch
import youtubedownload
import nightcorify
import deletesong
import asyncio

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='n`', help_command=None)

def main():
    print("Ready to sing!")
    bot.run(TOKEN)

@bot.command(name="play")
async def play(ctx, *, search: str): 
    try:
        connection = ctx.author.guild.voice_client
        await connection.disconnect()
    except AttributeError:
        pass

    channel = ctx.author.voice.channel
    if channel is None:
        await ctx.send("Must be in a voice channel")
    if("www.youtube.com" not in search):
        result = await youtubesearch.search_youtube(search)
        if result[0] is False:
            await ctx.send("Could not play song")
        vID = result[1]
    else:
        vID = search[-11:]
    filename = await youtubedownload.download_song(vID)
    
    if channel:
        vc = await channel.connect()

    if not vc.is_playing():
        vc.play(discord.FFmpegPCMAudio(source = 'D:\....Coding\discordnightcorebot\songs\Temp.mp3'))
        while(vc.is_playing()):
            await asyncio.sleep(1.0)
    deletesong.emptysongsfolder()
        
@bot.command(name="stop")
async def play(ctx):
    connection = ctx.author.guild.voice_client
    await connection.disconnect()

@bot.command(name="nightcore")
async def play(ctx, *, search: str):
    try:
        connection = ctx.author.guild.voice_client
        await connection.disconnect()
    except AttributeError:
        pass

    channel = ctx.author.voice.channel
    if channel is None:
        await ctx.send("Must be in a voice channel")
    if("www.youtube.com" not in search):
        result = await youtubesearch.search_youtube(search)
        if result[0] is False:
            await ctx.send("Could not play song")
        vID = result[1]
    else:
        vID = search[-11:]
    filename = await youtubedownload.download_song(vID)
    nightcorify.nightcore()
    await asyncio.sleep(6.0)
    if channel:
        vc = await channel.connect()

    if not vc.is_playing():
        vc.play(discord.FFmpegPCMAudio(source = 'D:\....Coding\discordnightcorebot\songs\Tempnightcore.mp3'))
        while(vc.is_playing()):
            await asyncio.sleep(1.0)
    deletesong.emptysongsfolder()

if __name__ == "__main__":
    main()