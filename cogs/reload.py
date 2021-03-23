from discord.ext import commands
import discord
import os
from os import listdir
from os.path import isfile, join

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    @commands.command()
    async def reload(self, ctx):
        if ctx.author.id in self.config["admin"]:
            embed = discord.Embed(description="Bot yenileniyor...", color=discord.Color.from_rgb(175, 238, 238))
            message = await ctx.send(embed=embed)
            for file in [f for f in listdir("cogs") if isfile(join("cogs", f))]:
                if file.endswith(".py"):
                    cog = f"cogs.{file[0:-3]}"
                    try:
                        self.bot.reload_extension(cog)
                    except Exception as e:
                        embed = discord.Embed(description=f"{cog[5:].capitalize()} yüklenemedi.\n\n```py\n{e}```", color=discord.Color.from_rgb(255, 0, 0))
                        return await message.edit(embed=embed)
            embed = discord.Embed(description="Bot başarıyla yenilendi.", color=discord.Color.from_rgb(0, 255, 0))
            return await message.edit(embed=embed)


def setup(bot):
    bot.add_cog(Reload(bot))
