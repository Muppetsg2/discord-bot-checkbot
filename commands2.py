import calendar
from datetime import datetime
from export import *
import discord
import pytz

async def le(ctx, l):

    if l == None:

        day = calendar.day_name[datetime.today().weekday()]
        pl = ""

        if day == "Monday":
            pl = "Poniedziałek"
        elif day == "Tuesday":
            pl = "Wtorek"
        elif day == "Wednesday":
            pl = "Środa"
        elif day == "Thursday":
            pl = "Czwartek"
        elif day =="Friday":
            pl = "Piątek"
        elif day == "Saturday":
            pl = "Sobota"
        elif day == "Sunday":
            pl = "Niedziela"

        plan = readPlan(day)

        embedVar=discord.Embed(title="Plan Lekcji", description=f'**{pl}**', color=0xff4100, timestamp = datetime.now(pytz.timezone('Europe/Warsaw')))
        embedVar.set_footer(text=f'{ctx.bot.user.name} @{versionValue()} | Marceli Antosik')

        for item in plan:
            embedVar.add_field(name=item, value=plan[item], inline=False)
    else:

        day = ""
        pl = ""
        if l.lower() == "poniedziałek":
            day = "Monday"
            pl = "Poniedziałek"
        elif l.lower() == "wtorek":
            day = "Tuesday"
            pl = "Wtorek"
        elif l.lower() == "środa":
            day = "Wednesday"
            pl = "Środa"
        elif l.lower() == "czwartek":
            day = "Thursday"
            pl = "Czwartek"
        elif l.lower() == "piątek":
            day = "Friday"
            pl = "Piątek"
        elif l.lower() == "sobota":
            day = "Saturday"
            pl = "Sobota"
        elif l.lower() == "niedziela":
            day = "Sunday"
            pl = "Niedziela"
        elif l.lower() == "monday":
            day = "Monday"
            pl = "Poniedziałek"
        elif l.lower() == "tuesday":
            day = "Tuesday"
            pl = "Wtorek"
        elif l.lower() == "wednesday":
            day = "Wednesday"
            pl = "Środa"
        elif l.lower() == "thursday":
            day = "Thursday"
            pl = "Czwartek"
        elif l.lower() == "friday":
            day = "Friday"
            pl = "Piątek"
        elif l.lower() == "saturday":
            day = "Saturday"
            pl = "Sobota"
        elif l.lower() == "sunday":
            day = "Sunday"
            pl = "Niedziela"
        else:
            await ctx.message.channel.send("Źle wpisałeś/aś nazwę tygodnia 😥")
            return "0"

        plan = readPlan(day)

        embedVar=discord.Embed(title="Plan Lekcji", description=f'**{pl}**', color=0xff4100, timestamp = datetime.now(pytz.timezone('Europe/Warsaw')))
        embedVar.set_footer(text=f'{ctx.bot.user.name} @{versionValue()} | Marceli Antosik')

        for item in plan:
            embedVar.add_field(name=item, value=plan[item], inline=False)

    return "1", embedVar

async def h(ctx):

    prefix = prefixValue()

    helpLines = [
        (f'@{ctx.bot.user.name}', "Pomoże zapoznać się z funkcjami bota ☺", False),
        (f'@{ctx.bot.user.name} prefix', "Pozwoli poznać prefix dla tego bota.", False),
        (f'{prefix}help', "Komenda pozwalająca spojrzeć na liste komend. **Lista jest wysyłana na kanał, gdzie została użyta komenda.**", False),
        (f'{prefix}dmhelp', "Komenda pozwalająca spojrzeć na liste komend. **Lista jest wysyłana do autora komendy.**", False),
        (f'{prefix}setUser', "Komenda do ustawienia roli po której sprawdza sie obecność", False),
        (f'{prefix}spr', "Komenda do sprawdzania obecności. Argumenty oznaczające dane grupy językowe [S, W, G, Z, R]. Jeśli lekcja jest dla wszystkich nie potrzeba wpisywać argumentu po wpisaniu komendy. **WAŻNE: Argumenty muszą byc poprzedzone przecinkiem i można w jednej komedzie wywołać tylko jeden argument! Osoba wywołująca funkcje musi znajdować się na kanale glosowym!**", False),
        (f'{prefix}lekcje', "Komenda pozwalająca na wyświetlenie planu lekcji na dany dzień. Można po spacji wpisać dzień tygodnia po polsku (uwzględniając wszystkie litery nawet ś,ć) lub po angielsku. W obu wariantach nie ważna jest wielkość liter. Jeśli po spacji nie zostanie wpisany dzień to zostanie podany plan lekcji na dzień aktualny. **UWAGA: Plan lekcji jest wysyłany na czat**", False),
        (f'{prefix}dmlekcje', "Komenda pozwalająca na wyświetlenie planu lekcji na dany dzień. Można po spacji wpisać dzień tygodnia po polsku (uwzględniając wszystkie litery nawet ś,ć) lub po angielsku. W obu wariantach nie ważna jest wielkość liter. Jeśli po spacji nie zostanie wpisany dzień to zostanie podany plan lekcji na dzień aktualny. **UWAGA: Plan lekcji jest wysyłany tylko do autora komendy**", False),
        (f'{prefix}ping', "Pong", False),
        (f'{prefix}invite', "Bot wysyła link do zaproszenia i liste pozwoleń które potrzebuje mieć na serwerze.", False)
    ]

    embedVar=discord.Embed(title="Help", description="Kilka komend które mogą być przydatne 😉", color=0xe80325, timestamp = datetime.now(pytz.timezone('Europe/Warsaw')))
    embedVar.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar_url)
    embedVar.set_thumbnail(url=ctx.bot.user.avatar_url)
    embedVar.set_footer(text=f'{ctx.bot.user.name} @{versionValue()} | Marceli Antosik')

    for name,value,inline in helpLines:
        embedVar.add_field(name=name,value=value,inline=inline)
    
    return embedVar

async def inv(ctx):

    permissions = [
        ('Pozwolenie 1:', "✅ Wyświetlanie kanałów", False),
        ('Pozwolenie 2:', "✅ Wysyłanie wiadomości", False),
        ('Pozwolenie 3:', "✅ Zamieszczanie wzmianek @everyone, @here oraz wszystkich ról", False),
        ('Pozwolenie 4:', "✅ Zarządzanie wiadomościami", False),
        ('Pozwolenie 5:', "✅ Czytanie historii czatu", False)
    ]

    embedVar=discord.Embed(title="Jeśli chcesz mnie zaprosić na inny serwer, proszę kliknij w link poniżej.", description="Co Ja potrzebuje:", color=0xe80325, timestamp = datetime.now(pytz.timezone('Europe/Warsaw')))
    embedVar.set_thumbnail(url=ctx.bot.user.avatar_url)
    embedVar.set_footer(text=f'{ctx.bot.user.name} @{versionValue()} | Marceli Antosik')

    for name,value,inline in permissions:
        embedVar.add_field(name=name,value=value,inline=inline)

    
    return embedVar

async def sprawdz(ctx):

    channelID = ctx.message.author.voice.channel.id
    room = ctx.bot.get_channel(channelID).voice_states

    napisyP = ["Lista obecności:", "Nieobecni:", "Liczba Uczniów:", "Imiona Nieobecnych:"]

    nm = "Nie ma takich osób 😁"

    napisy = []

    i = 0

    args = ctx.message.content.split(' ')

    if len(args) > 1:

        if args[1] == "A": #Angielski
            numery = [3,4,5,6,8,12,15,16,17,18,19,20,21,22,25]
            napisy = napisyP
            m = len(numery)
        elif args[1] == "F": #Francuski
            numery = [1,2,7,9,10,11,13,14,23,24,26]
            napisy = napisyP
            m = len(numery)
        else:
            await ctx.message.channel.send("Nie ma takiej grupy 😥")
            return "0"
    else:
        numery = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        napisy = napisyP
        m = len(numery)

    for person in room:

        man = await ctx.message.guild.fetch_member(person)

        if len(man.roles) > 1:

            roles = man.roles

            for role in roles:

                if role.id == readUserTag():
                    i += 1
                    try:
                        num = int(man.display_name[0:2])
                        numery.remove(num)
                    except:
                        await ctx.message.channel.send(f'<@!{person}> ma zły pseudonim a podaje się za ucznia **(nie posiada numeru na początku)**')
    
    text = ""
    imiona = ""
    z = 0

    for letter in numery:
        if z > 0:
            text += f', {letter}'
            imiona += f', {getNumbers(str(letter))}'
        else:
            text += str(letter)
            imiona += getNumbers(str(letter))
        z+=1

    if text == "":
        text = nm

    if imiona == "":
        imiona = nm

    embedVar=discord.Embed(title=ctx.message.author.voice.channel.name, description=napisy[0], color=0xff4100, timestamp = datetime.now(pytz.timezone('Europe/Warsaw')))
    embedVar.add_field(name=napisy[1], value=text, inline=True)
    embedVar.add_field(name=napisy[2], value=f'{i}/{m}', inline=True)
    embedVar.add_field(name=napisy[3], value=imiona, inline=False)
    embedVar.set_footer(text=f'{ctx.bot.user.name} @{versionValue()} | Marceli Antosik')

    return "1",embedVar