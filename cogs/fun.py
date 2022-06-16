from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        pass

    # commands
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yas - definitely.",
                "You may rely on it.",
                "As I see it, yas.",
                "Most likely.",
                "Outlook good.",
                "Yas.",
                "Signs point to yas.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(Fun(bot))