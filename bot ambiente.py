import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name='consejos')
async def consejos(ctx):
    consejos_list = [
        "Reduce el uso de plástico desechable.",
        "Utiliza botellas reutilizables para agua.",
        "Apaga las luces cuando no las necesites.",
        "Separa tus residuos de manera adecuada.",
        "Compra productos con menos empaques.",
        "Reutiliza frascos y recipientes en casa.",
        "Opta por transporte público o bicicleta para moverte.",
    ]
    response = "Consejos para cuidar el medio ambiente:\n" + "\n".join(f"- {consejo}" for consejo in consejos_list)
    await ctx.send(response)

@bot.command(name='separar')
async def separar(ctx):
    separacion_list = [
        "Plásticos: Botellas de agua, envases de alimentos.",
        "Vidrio: Frascos y botellas limpias.",
        "Papel y cartón: Periódicos, revistas, cajas de cereal.",
        "Orgánicos: Restos de comida y cáscaras de frutas.",
        "Metales: Latas de aluminio y hojalata.",
        "No reciclables: Papel higienico, envolturas sucias, etc."
    ]
    response = "Guía para separar los residuos:\n" + "\n".join(f"- {item}" for item in separacion_list)
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

bot.run('MTMyNzQ1ODYyMjM2MzY2NDQ4NQ.GlA-S5.nwJqT_JecvkZWwNXC-xaKEXrtE6hrySCORpwj4')
