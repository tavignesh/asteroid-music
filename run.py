import discord
import psutil
import time
from time import perf_counter
import asyncio
import uptime
import platform
import math

# strtuptime = int(uptime.uptime())

client = discord.Client()

toktok = "ODM2ODMwMDkzNjQ0NzkxODA5.YIjswQ.kBRoAp1xdvvbkoS8VaI3lTdzQhA"

invitembd = discord.Embed(title=" <a:ag_reddot:781410740619051008> **Usefull Links** <a:ag_reddot:781410740619051008> \n▬▬▬▬▬▬▬▬▬▬", description="<a:ag_arrowgif:781395494127271947> [Invite Asteroid Music](https://discord.com/oauth2/authorize?client_id=836830093644791809&scope=bot&permissions=37080400) :notes: \n<a:ag_arrowgif:781395494127271947> [Invite Asteroid](https://discord.com/oauth2/authorize?client_id=780472070072696852&scope=bot&permissions=809500159)  <a:ag_tickop:781395575962599445> \n<a:ag_arrowgif:781395494127271947> [Vote Asteroid](https://top.gg/bot/780472070072696852/vote)\n<a:ag_arrowgif:781395494127271947> [Support Server](https://discord.gg/teszgSR9yK) <a:ag_discord:781395597277134869>\n<a:ag_arrowgif:781395494127271947> [Asteroid Gaming](https://discord.gg/CjKRmV7ptm) <a:ag_discord:781395597277134869>", color=0x13FD03)


@client.event
async def on_ready():
    if toktok == "":
        print("no token specified")
    else:
        # game = discord.Game("With 『AG』》Vigne$hᴰᵉᵛ#8351 am/ help")
        game = discord.Game("and Singing Songs in a lot of Servers!")
        await client.change_presence(status=discord.Status.idle, activity=game)
        # await client.change_presence(status=discord.Status.online, activity=game)
        # await client.change_presence(status=discord.Status.invisible, activity=game)
        # await client.change_presence(status=discord.Status.do_not_disturb, activity=game)
    print("{} music is ONLINE!!".format(client.user))

@client.event
async def on_message(message):
    global messages

    print("The Message | ", message.content, " | Was sent in | ", message.channel, " | Channel by | ", message.author, "| in SERVER =>", message.guild)

    if message.content.startswith('am/ music') or message.content == 'am/ help music' or message.content == 'am/ music help' or message.content.startswith('am/ help') or message.content.startswith('am/music') or message.content == 'am/music help' or message.content.startswith('am/help'):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Asteroid Music :notes:\n▬▬▬▬▬▬▬▬▬▬", description="**Music:**\nAsteroid Music allows you to listen to music by streaming music to a voice channel. To activate all commands join a voice channel and use `am/ play songname`. This also includes a lot of filters which can be applied to the song!!. Enjoy the music and kindly report any bugs or gliches to [Support Server](https://discord.gg/teszgSR9yK)\n__Music Commands (Usage: `am/ command`)__:\nplay, pause, clear-queue, filter, loop, nowplaying, queue, resume, search, shuffle, skip, stop, volume, w-filters\n__Filters (Usage: `am/ filter filtername`)__:\n`8D, gate, haas, phaser, treble, tremolo, vibrato, reverse, karaoke, flanger, mcompand, pulsator, subboost, bassboost, vaporwave, nightcore, normalizer, surrounding`\n\n**Invite:** Use `am/invite`\n\n**Suggestions:**:\nYour Suggesions are Really Valuable to us(me) , It helps in Improving The Bot!\n__Syntax:__ `am/ suggest <your suggesion>`\n__Example:__\n`am/ suggest add more effects`\n\n**Stats:**\nCPU Spec:`am/ cpu`\nLatency:`am/ ping`\nServer Count: `am/ servers`", color=0xBCFC09))

    if message.content.find("am/ cpu") != -1 or message.content.find("am/cpu") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if str(platform.system()) != "":
            pass
            cpupert = psutil.cpu_percent()
            cpun = psutil.cpu_count()
            cpusw = psutil.swap_memory()
            cpupers = psutil.cpu_percent(percpu=1)

            cpui = psutil.cpu_freq()
            cpui = str(cpui)
            cpui = cpui.split("=")[-1]
            cpui = cpui.split(")")[0]
            cpui = float(cpui)
            cpui = cpui / 1000
            cpuppp = ""
            print("printing hereeeeee: ", cpupers)
            for i in range(len(cpupers)):
                cpuo = cpupers[int(i)]
                cpuppp += f"Core{int(i)}: {cpuo}%\n"

            cpusw = str(cpusw)
            cpuswt = cpusw.split("=")[1]
            cpuswt = cpuswt.split(",")[0]
            cpuswt = float(cpuswt)
            cpuswt = cpuswt/10000000
            cpuswt = math.floor(cpuswt)
            cpuswt = cpuswt/100

            cpusw = str(cpusw)
            cpuswu = cpusw.split("=")[2]
            cpuswu = cpuswu.split(",")[0]
            cpuswu = float(cpuswu)
            cpuswu = cpuswu / 10000000
            cpuswu = math.floor(cpuswu)
            cpuswu = cpuswu / 100

            cpusw = str(cpusw)
            cpuswf = cpusw.split("=")[3]
            cpuswf = cpuswf.split(",")[0]
            cpuswf = float(cpuswf)
            cpuswf = cpuswf / 10000000
            cpuswf = math.floor(cpuswf)
            cpuswf = cpuswf / 100

            cpusw = str(cpusw)
            cpuswp = cpusw.split("=")[4]
            cpuswp = cpuswp.split(",")[0]

            sysarch = platform.architecture()[0]
            nodsds = platform.node()
            sysmchn = platform.system()

            dist = platform.dist()
            dist = " ".join(x for x in dist)

            with open("/proc/meminfo", "r") as f:
                lines = f.readlines()

            meminf1 = ("     " + lines[0].strip())
            meminf2 = ("     " + lines[1].strip())

            with open("/proc/cpuinfo", "r")  as f:
                info = f.readlines()

            syscpumo = "Error"
            cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
            for index, item in enumerate(cpuinfo):
                syscpumo = ("    " + str(index) + ": " + item)

            uptime = None
            with open("/proc/uptime", "r") as f:
                uptime = f.read().split(" ")[0].strip()
            uptime = int(float(uptime))
            uptime_hours = uptime // 3600
            uptime_minutes = (uptime % 3600) // 60
            servuptime = ("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

            with open("/proc/loadavg", "r") as f:
                avgload = ("Average Load: " + f.read().strip())
            sysspd = syscpumo.split(" ")[-1]
            await message.channel.send(embed=discord.Embed(title="CPU STATS :tools:", description=f"\nNode: {nodsds}\nServer Load: {avgload}\n\n**Processor**\nArchitecture: {sysarch}\nModel: {syscpumo}\nCores = {cpun}\nSpeed = {sysspd} Ghz\nTotal Usage = {cpupert}%\n{cpuppp}\n\nOS: {sysmchn}\nDist: {dist}\n\nDisk:\nTotal: {meminf1}\nFree: {meminf2}\n\n**RAM**\nTotal = {cpuswt} Gb\nUsed = {cpuswu} Gb\nPercentage = {cpuswp}%\nFree = {cpuswf} Gb\n\nServer {servuptime}", color=0xFD9E01))

    if message.content.startswith("am/ suggest ") or message.content.startswith("am/ suggest "):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        msglst = message.content.split(" ")
        if len(msglst) >= 3:
            sugg = ""
            for i in range(2, len(msglst)):
                sugg = f"{sugg} {msglst[i]} "
            await message.channel.send(embed=discord.Embed(title=" <a:ag_reddot:781410740619051008> Suggested! <a:ag_reddot:781410740619051008> ", description="Thanks for Your Valuable Suggestion!\nYour Suggestion Has Been Submitted in our Support server! <a:ag_tickop:781395575962599445> ", color=0x04FD03))
            channel = client.get_channel(784697044236763176)
            sogs = await channel.send(embed=discord.Embed(title=f" <a:ag_reddot:781410740619051008> Suggestion by :**{message.author}** From **{message.guild}** for Asteroid Music <a:ag_reddot:781410740619051008> ", description=f"`{sugg}`", color=0x04FD03))
            await sogs.add_reaction('👍')
            await sogs.add_reaction('👎')
        else:
            await message.channel.send("**A suggestion cannot be blank!**")

    if message.content.startswith("am/ invite") or message.content.startswith("am/ support") or message.content.startswith("am/invite") or message.content.startswith("am/support"):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=invitembd)

    if message.content.find("am/ ping") != -1 or message.content.find("am/ uptime") != -1 or message.content.find("am/ping") != -1 or message.content.find("am/uptime") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        start = perf_counter()
        mesa = await message.channel.send(embed=discord.Embed(title="Pinging... <a:ag_ldingwin:781410586138902529>", description="May take some time..", color=0x09BEFC))
        end = perf_counter()
        duration = (end - start) * 1000
        duration = math.floor(duration)
        ping = client.latency
        ping = ping * 1000
        ping = math.floor(ping)
        # enduptime = int(uptime.uptime())
        # uptimm = int(enduptime - strtuptime)
        # upsec = uptimm
        # upmin = 0
        # uphr = 0
        # upday = 0
        # if uptimm > 59:
        #     upsec = uptimm % 60
        #     upmin = int(uptimm / 60)
        #     if upmin > 60:
        #         upmin = int(upmin % 60)
        #         uphr = int(upmin / 60)
        #         if uphr > 24:
        #             uphr = uphr % 24
        #             upday = int(uphr / 24)
        await mesa.edit(embed=discord.Embed(title="Pings and Pongs <a:ag_ggl:781410701327335445>", description=f":alarm_clock: API Ping: {ping}ms\n:satellite: Latency: {duration}ms\n:hourglass: Total Ping: {ping + duration}ms\n\nUptime: Error\nNode: US1", color=0x02BDFE))

    if message.content.startswith("am/ server") or message.content.startswith("am/server"):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        tserver = len(client.guilds)
        await message.channel.send(embed=discord.Embed(title="Server Count", description=f"Playing Music in {tserver} Servers <a:ag_tickop:781395575962599445> Now \nWOW!!" , color=0x01FD59))

    if message.content.startswith("am/ server list") or message.content.startswith("am/server list"):
        if str(message.author.id) == "641305773095387156":
            await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            serverlst = client.guilds
            serverstr = ""
            for i in range(0,len(serverlst)):
                serverstr = f"{serverstr}\n{serverlst[i]}"
            await message.channel.send(embed=discord.Embed(title="Server List", description=f"{serverstr}" , color=0x01FD59))

    if message.content == ("am/") or message.content == ("am/ "):
        await message.channel.send(embed=discord.Embed(title="Yes? , How May i Help You?", description=("Use `am/ help` for More!"), color=0x04FD03))
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    
    if message.content == "<@!836830093644791809>":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="My prefix is `am/`", color=0x04FD03))


client.run(toktok)
