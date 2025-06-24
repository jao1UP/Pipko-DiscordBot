
import discord, os
from discord.ext import commands, tasks
from discord import SelectOption, app_commands
from dotenv import load_dotenv
import os

intents = discord.Intents.all()
bot = commands.Bot(".", intents= intents)

load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    sinc = await bot.tree.sync()
    print(f"{len(sinc)} comandos sincronizados com sucesso!")
    print(f"bot online! {bot.user.name} - {bot.user.id}")
    
@bot.command()
async def online(ctx:commands.Context):
    await bot.change_presence(activity = discord.CustomActivity(
    name = "🐱 Estou online gente!"
    ))
    await ctx.send("Status atualizado! O bot está online! 🐱")
@bot.command()
async def dormindo(ctx:commands.Context):
    await bot.change_presence(activity = discord.CustomActivity(
    name = "😴 Hora de descansar!"
    ))
    await ctx.send("Status atualizado! dormindo! 🐱")



@bot.event
async def on_member_join(membro:discord.Member):
    minha_embed = discord.Embed()
    minha_embed.title = "Bem vindo ao servidor!"
    minha_embed.description = f"{membro.mention} Seja bem vindo ao servidor!"
    minha_embed.color = discord.Color.yellow()
    imagem = discord.File("pipko_animacao.gif", "pipko.gif")
    minha_embed.set_image(url="attachment://pipko.gif")
    minha_embed.set_footer(text="Espero que se divirta aqui!")
    canal = bot.get_channel(758565643074666498)

    await canal.send(embed=minha_embed, file=imagem)


@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.mention
    await ctx.send(f"Oii {nome}! tudo bem?")

@bot.event #enviou mensagem
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    canal = bot.get_channel(1385831519700123698)
    await canal.send(f"O {msg.author.mention} enviou uma mensagem no canal {msg.channel.mention} com o conteudo: {msg.content}")
    await bot.process_commands(msg)

@bot.event
async def on_message_delete(msg:discord.Message):
    canal = bot.get_channel(1385831519700123698)
    embed2 = discord.Embed(title="Mensagem deletada", description=f"A mensagem do {msg.author.mention} foi deletada no canal {msg.channel.mention} com o conteudo: {msg.content}", color=discord.Color.red())

    await canal.send(embed=embed2)



@bot.tree.command()
async def enquete(interaction: discord.Interaction, pergunta: str):
    embed = discord.Embed(
        title= f"Enquete gerada por {interaction.user.name}",
        description=pergunta,
        color=discord.Color.yellow()
    )
    mensagem = await interaction.channel.send(embed=embed)
    await mensagem.add_reaction("✅")
    await mensagem.add_reaction("❌")
    await interaction.response.send_message("✅ Enquete criada com sucesso!", ephemeral=True)



@bot.tree.command()
async def ping(interact:discord.Interaction):
    await interact.response.send_message(f"Pong! Latência: {round(bot.latency * 1000)}ms", ephemeral=True)


bot.run(TOKEN)
