from discord.ext import commands, tasks
import discord

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="start",
        description="Starts the server",
    )
    async def start(self, ctx):
        await ctx.send(self.bot.server.StartServer())

    @commands.command(
        name="status",
        description="Gets the status of the server",
    )
    async def status(self, ctx):
        await ctx.send(self.bot.server.GetStatus())

    @commands.command(
        name="info",
        description="Gets the info of the server",
    )
    async def info(self, ctx):
        await ctx.send(self.bot.server.GetServerInfo())


def setup(bot):
    bot.add_cog(Commands(bot))