import os
try:
  import discord
except:
  os.system("pip install discord")
try:
  import requests
except:
  os.system("pip install requests")
import time
import random
import configparser
from discord.ext import commands, tasks
from colorama import Fore, init

init()
clear = lambda: os.system('cls')
cfg = configparser.ConfigParser()
cfg.read("config.ini")
token = cfg.get("Config", "Token")

client = commands.Bot(command_prefix=[">", "ю", "Ю"], self_bot=True)

decoratorone = "╔=====================================╗"
decoratortwo = "╚=====================================╝"

clear()
print(f"""{Fore.LIGHTBLUE_EX}
███████ ███    ███ ██████  ███████ ██████  
██      ████  ████ ██   ██ ██      ██   ██ 
█████   ██ ████ ██ ██████  █████   ██   ██ 
██      ██  ██  ██ ██   ██ ██      ██   ██ 
███████ ██      ██ ██████  ███████ ██████  
    """)
print("""

 ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
 ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
                                                                             
                                                                             
""")

@client.event
async def on_ready():
    print("Всё готово к работе.")

@client.command(aliases=['e', 'em', 'emb', 'у', 'уь', 'уьи', 'уьиув', 'е', 'э', 'ем', 'эм', 'емб', 'эмб', 'ембед', 'эмбед', 'ю', 'Ю', '>', '.'])
async def embed(ctx, *, arg):
    params = {'description': arg, 'color': cfg.get("Config", "Color")}
    result = requests.get('https://em.0x71.cc/', params=params)
    t = await ctx.message.edit(content = f"https://em.0x71.cc/{result.text}")
    print(f"{decoratorone}\nБыл отправлен эмбед \nСодержание: {Fore.LIGHTGREEN_EX}{arg}{Fore.LIGHTBLUE_EX}\n")
    try:
        print(f"Cервер: {t.guild.name}\nКанал:{t.channel}\n{decoratortwo}")
    except:
        print(f"Сервер: Нет\nКанал: Нет\n{decoratortwo}")

client.run(token, bot=False)
