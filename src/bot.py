import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='n`', help_command=None)

def main():
    print("Ready to sing!")
    bot.run(TOKEN)

@bot.command(name="play")
async def play(ctx, *, search: str):
    await ctx.send(f"Ayy bitch you wanted me to play, {search}?")



if __name__ == "__main__":
    main()