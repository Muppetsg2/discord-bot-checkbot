from discord.ext import commands
from commands2 import *
from export import *
from datetime import datetime

# Importy przechodzą z plików commands2 i export, nie ma potrzeby ich powtarzać

client = commands.Bot(command_prefix=prefixValue(), help_command=None)


@client.event
async def on_ready():
    # Nazwa 'time' jest już używana w całym pliku, shadowing może być źródłem błędów w przyszłości
    time_ = datetime.now(pytz.timezone('Europe/Warsaw')).strftime('%H:%M')

    print('Logged in as {0}! 🤖'.format(client.user))
    print(f'Logged at {time_} ⏰')

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Vibing 🎶"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<@') and str(len(message.mentions)) == "1" and message.mentions[0].id == 814851090029215784:
        args = message.content.split(' ')

        if len(args) > 1:
            if args[1] == "prefix":
                embedVar = discord.Embed(title="Prefix:", description=f'`{await get_prefix_value()}`', color=0xe80325, timestamp=datetime.now(pytz.timezone('Europe/Warsaw')))
                embedVar.set_footer(text=f'{client.user.name} @{await get_version_value()} | Marceli Antosik')
                await message.delete()
                await message.channel.send(embed=embedVar)
            else:
                await message.channel.send("Po co mnie pingujesz?")

        else:
            await message.delete()
            await message.channel.send("Jeśli nie wiesz co ja potrafie po prostu wpisz `{0}help` lub `{0}dmhelp`".format(await get_prefix_value()))  # Zapobiegamy podwójnemu uruchomieniu funkcji

    await client.process_commands(message)


# error handler dla wszystkich komend
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.channel.send('Proszę wprowadzić wszystkie wymagane argumenty')

    # Użycie elif jest tutaj bardziej optymalne, ponieważ podane typy błędów nie mogą się nakładać
    elif isinstance(error, commands.BotMissingPermissions):
        permissions = [
            ('Pozwolenie 1:', "✅ Wyświetlanie kanałów", False),
            ('Pozwolenie 2:', "✅ Wysyłanie wiadomości", False),
            ('Pozwolenie 3:', "✅ Zamieszczanie wzmianek @everyone, @here oraz wszystkich ról", False),
            ('Pozwolenie 4:', "✅ Zarządzanie wiadomościami", False),
            ('Pozwolenie 5:', "✅ Czytanie historii czatu", False)
        ]

        embedVar = discord.Embed(title="Nie posiadam któregoś z tych uprawnień:", color=0xff4100, timestamp=datetime.now(pytz.timezone('Europe/Warsaw')))
        embedVar.set_thumbnail(url=ctx.bot.user.avatar_url)
        embedVar.set_footer(text=f'{ctx.bot.user.name} @{await get_version_value()} | Marceli Antosik')

        for name, value, inline in permissions:
            embedVar.add_field(name=name, value=value, inline=inline)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.channel.send('Nie znam jeszcze takiej komendy. Przykro mi 😥')
    elif isinstance(error, commands.TooManyArguments):
        ctx.message.channel.send("Zbyt dużo argumentów")

    # Może tak? Nie widzę za bardzo potrzeby wymieniania tych wszystkich błędów, ale nie wiem co miałeś na myśli
    else:
        raise error


@client.command(name="ping")
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')


@client.command(name="lekcje", pass_context=True)
async def lekcje(ctx, l=None):
    embedVar = await le(ctx, l)

    if embedVar[0] == "1":
        await ctx.message.channel.send(embed=embedVar[1])


@client.command(name="dmlekcje", pass_context=True)
async def dmlekcje(ctx, l=None):
    embedVar = await le(ctx, l)

    if embedVar[0] == "1":
        await ctx.message.delete()
        await ctx.message.author.send(embed=embedVar[1])


@client.command(name="help", pass_context=True)
async def help(ctx):
    embedVar = await h(ctx)

    await ctx.message.channel.send(embed=embedVar)


@client.command(name="dmhelp", pass_context=True)
async def dmhelp(ctx):
    embedVar = await h(ctx)

    await ctx.message.delete()
    await ctx.message.author.send(embed=embedVar)


@client.command(name="invite", pass_context=True)
async def invite(ctx):
    embedVar = await inv(ctx)

    await ctx.message.delete()
    await ctx.message.author.send(embed=embedVar)
    await ctx.message.author.send(await asyncio.get_event_loop().run_in_executor(None, inviteValue))


@client.command(name="setUser", pass_context=True)
async def setUser(ctx, mention=None, *args):
    if len(args) == 0:
        if mention.startswith('<@'):
            await asyncio.get_event_loop().run_in_executor(None, writeUserTag, ctx.message.role_mentions[0].id)
            embedVar = discord.Embed(title="Sukces", description="Ustawiono rolę:", color=0x17d130, timestamp=datetime.now(pytz.timezone('Europe/Warsaw')))
            embedVar.set_footer(text=f'{ctx.bot.user.name} @{await get_version_value()} | Marceli Antosik')
            embedVar.add_field(name=f'@{ctx.message.role_mentions[0]}:', value="jako uczeń", inline=True)
            await ctx.message.channel.send(embed=embedVar)
        else:
            await ctx.message.channel.send('Musisz podać rolę!')

    elif len(args) > 0:
        await ctx.message.channel.send('Podaj jedną rolę!')

    else:
        await ctx.message.channel.send('Musisz podać rolę!')


@client.command(name="spr", pass_context=True)
async def spr(ctx):
    # W pythonie do porównywania z None używamy 'is None' zamiast ==
    if ctx.message.author.voice is not None:
        embedVar = await sprawdz(ctx)

        if embedVar[0] == "1":
            await ctx.message.channel.send(embed=embedVar[1])

    else:
        await ctx.message.channel.send(f'<@!{ctx.message.author.id}> musisz być na kanale głosowym')


client.run(tokenValue())
