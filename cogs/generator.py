from discord.ext import commands
import discord
import random
import time

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='steamkey')
    async def steamkey(self, message):
        bot = self.bot
        config = bot.config
        steamkey = open('config/steamkey.txt').read().splitlines()
        if message.channel.id == bot.config["channels"]["steam"]:
            key = random.choice(steamkey)
            embed = message.reply(color=0x00ff37, description=f"{key}")
            await message.reply(embed=embed, mention_author=True)
        else:
            embed = discord.Embed(color=0xff0000, description=f"<#{bot.config['channels']['steam']}> kanalını kullanın.")
            await message.reply(embed=embed, mention_author=True)

    @commands.command(name='mcpre')
    async def mcpre(self, message):
        bot = self.bot
        config = bot.config
        steamkey = open('config/mcpre.txt').read().splitlines()
        if message.channel.id == bot.config["channels"]["minecraft"]:
            key = random.choice(steamkey)
            embed = discord.Embed(color=0x00ff37, description=f"{key}")
            await message.reply(embed=embed, mention_author=True)
        else:
            embed = discord.Embed(color=0xff0000, description=f"<#{bot.config['channels']['minecraft']}> kanalını kullanın.")
            await message.reply(embed=embed, mention_author=True)
            
def setup(bot):
    bot.add_cog(Commands(bot))
