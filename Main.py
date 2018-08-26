import random
import discord
import asyncio
import json
import io
import time
import requests
from tkinter import *
import datetime



players = {}

client = discord.Client()



VERMELHO = 0xFF0000
COMANDOS = 0x2EFEF7
COR = 0x6FE96B
msg_id = None
msg_user = None
status = None
humano = None


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Team DxD Family'))
    print('-----------DxD-------------')
    print('Bot ONLINE - Ola Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('-----------DxD-------------')





@client.event
async def on_message(message):
    #----------------------------Comando Teste---------------------------------
    if message.content.lower().startswith('.teste'):
        await client.send_message(message.channel, "Olá Mundo, estou vivo!")
    #---------------------------Comando Da Moeda-------------------------------
    if message.content.lower().startswith('.moeda'):
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '👦🏽')
        if choice == 2:
            await client.add_reaction(message, '👑')
    #-----------------------------Matar o Jose--------------------------------
    if message.content.lower().startswith('matar o jose'):
        choice = random.randint(3,4)
        if choice == 3:
            await client.add_reaction(message, '✔')
        if choice == 4:
            await client.add_reaction(message, '❌')

    #----------------------------Comando DO SITE----------------------------------
    if message.content.lower().startswith('.site'):
        await client.send_message(message.channel, "o site é http://teamdxd.ml")
        await client.add_reaction(message, "👍")
    #----------------------------Comando Do Ts3------------------------------------
    if message.content.lower().startswith('.ts3'):
        await client.send_message(message.channel, "o TeamSpeak Do DxD é : TS3.TEAMDXD.ML")
        await client.add_reaction(message, "👍")
    #-------------------------------------------OI---------------------------------------------------
    if message.content.lower().startswith('.jose'):
        jose = await client.send_message(message.channel, "!fm xbox DxD GuiihSouza_ , DxD JuanZilla")
        await asyncio.sleep(2)  # 5 Segundos dps
        await client.delete_message(jose)
    #------------------------------------------Status-------------------------------------------------
    if message.content.lower().startswith('.status1'):
        await client.change_presence(game=discord.Game(name='Team DxD'))
        await client.send_message(message.channel, "Status do Bot Alterado Para 'Team DxD'!")
        await client.add_reaction(message, "👍")

    if message.content.lower().startswith('.status2'):
        await client.change_presence(game=discord.Game(name='DxD Family'))
        await client.send_message(message.channel, "Status do Bot Alterado Para 'DxD Family'!")
        await client.add_reaction(message, "👍")

    #----------------------------------Gifs---------------------------------------------
    prefix = "."
    if message.content.lower().startswith(prefix + "gif"):
        prefi = len(prefix) + 4
        tag = message.content[prefi:]
        apikey = "gNLNigwnrwtKvxHd8TXGFx3xSrvsGKyl"  # copie e cole sua api key aqui
        url = "http://api.giphy.com/v1/gifs/random?tag={}&api_key={}&rating=g".format(tag, apikey)
        r2 = json.loads(requests.get(url).text)
        link = r2['data']['images']['downsized_large']['url']
        imagem = requests.get(link, stream=True)  ## Caso queira colocar em uma Embed apague essa linha e a de baixo
        # e apague o import io.
        await client.send_file(message.channel, io.BytesIO(imagem.raw.read()), filename="Giphy.gif")
    #------------------------------------------Ping-------------------------------------------
    if message.content.lower().startswith('.ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=0x000000,
                                   description='Meu tempo de resposta é `{}ms`!'.format(round((t2 - t1) * 1000)))
        await client.send_message(message.channel, f"{message.author.mention}", embed=ping_embed)
    #------------------------------------------------Players----------------------------------------
    if message.content.lower().startswith('.info'):
        try:
            user = message.mentions[0]
            server = message.server
            embedinfo = discord.Embed(title='Informações do usuário', color=0x03c3f5, )
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='Usuário:', value=user.name)
            embedinfo.add_field(name='Apelido', value=user.nick)
            embedinfo.add_field(name='🆔 ID:', value=user.id)
            embedinfo.add_field(name='📅 Entrou em:', value=user.joined_at.strftime("%d %b %Y às %H:%M"))
            embedinfo.add_field(name='📅 Server criado em:', value=server.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='Jogando:', value=user.game)
            embedinfo.add_field(name="Status:", value=user.status)
            embedinfo.add_field(name='Cargos:', value=([role.name for role in user.roles if role.name != "@everyone"]))
            await client.send_message(message.channel, embed=embedinfo)
        except ImportError:
            await client.send_message(message.channel, 'Buguei!')
        except:
            await client.send_message(message.channel, '❎ | Mencione um usuário válido!')
        finally:
            pass
    #------------------------------------------Avatar--------------------------------
    prefixo = "."
    if message.content.startswith(prefixo + "avatar"):
        xtx = message.content.split(' ')
        if len(xtx) == 1:
            useravatar = message.author
            avatar = discord.Embed(
                title="Avatar de: {}".format(useravatar.name),
                color=VERMELHO,
                description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
            )

            avatar.set_image(url=useravatar.avatar_url)
            avatar.set_footer(text="Pedido por {}#{}".format(useravatar.name, useravatar.discriminator))
            await client.send_message(message.channel, embed=avatar)
        else:
            try:
                useravatar = message.mentions[0]
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=VERMELHO,
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

            except IndexError:
                a = len(prefixo) + 7
                uid = message.content[a:]
                useravatar = message.server.get_member(uid)
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=VERMELHO,
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

    #-----------------------------------------Teste-----------------------------------
    if message.content.lower().startswith('.ship'):
        try:
            cont = message.mentions[0].name
            cont2 = message.mentions[1].name
            cont3 = len(cont2)
            cont4 = cont3 - 4
            cont5 = cont[0:4]
            cont6 = cont2[cont4:cont3]
            cont7 = cont5 + cont6
            await client.send_message(message.channel,
                                      "Junção do nome de {} com {} = **{}**".format(message.mentions[0].mention,
                                                                                    message.mentions[1].mention, cont7))
        except IndexError:
            await client.send_message(message.channel,
                                      "{} Você não mencionou dois usuarios".format(message.author.mention))
    #----------------------------------------Apagar Msgs------------------------------
    prefixo = "."

    if message.content.lower().startswith(prefixo + "limpar"):

        try:
            if not message.author.server_permissions.administrator:
                await client.send_message(message.channel, "Voce nao tem permissao")
                return

            if message.author.server_permissions.administrator:
                a = len(prefixo) + 7
            if int(message.content[a:]) < 500:
                qntd = int(message.content[a:]) + 1
                await client.purge_from(message.channel, limit=qntd)
                cleared = await client.send_message(message.channel,
                                                    f'{qntd} mensagens foram apagadas por {message.author.mention}!')
                await asyncio.sleep(5)
                await client.delete_message(cleared)
            else:
                await client.send_message(message.channel, 'Você nao pode apagar mais de 500 mensagens de uma so vez!')
        except ValueError:
            await client.send_message(message.channel, 'Digite um valor para apagar')
        except discord.Forbidden:
            await client.send_message(message.channel, 'Não tenho permissões para apagar mensagens!')
        else:
            print(message.channel, "Voce Nao Tem Permissao Para Usar este Comandos")
    #---------------------------------------Server info--------------------------------
    if message.content.startswith('.serverinfo'):
        user = message.author.name

        horario = datetime.datetime.now().strftime("%H:%M:%S")

        serverinfo_embed = discord.Embed(title="\n", description="Abaixo está as informaçoes principais do servidor!",
                                         color=COR)
        serverinfo_embed.set_thumbnail(url=message.server.icon_url)
        serverinfo_embed.set_footer(text="{} • {}".format(user, horario))
        serverinfo_embed.add_field(name="Nome:", value=message.server.name, inline=True)
        serverinfo_embed.add_field(name="Dono:", value=message.server.owner.mention)
        serverinfo_embed.add_field(name="ID:", value=message.server.id, inline=True)
        serverinfo_embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        serverinfo_embed.add_field(name="Canais de texto:", value=len(
            [message.channel.mention for channel in message.server.channels if
             channel.type == discord.ChannelType.text]), inline=True)
        serverinfo_embed.add_field(name="Canais de voz:", value=len(
            [message.channel.mention for channel in message.server.channels if
             channel.type == discord.ChannelType.voice]), inline=True)
        serverinfo_embed.add_field(name="Membros:", value=len(message.server.members), inline=True)
        serverinfo_embed.add_field(name="Bots:",
                                   value=len([user.mention for user in message.server.members if user.bot]),
                                   inline=True)
        serverinfo_embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),
                                   inline=True)
        serverinfo_embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
        await client.send_message(message.channel, embed=serverinfo_embed)
    #------------------------------------Sorteio--------------------------------------
    if message.content.lower().startswith(".sorteio"):  # esse comandos sorteia um memebro
        if message.author.server_permissions.administrator:
            n = random.choice(list(message.server.members))
            n1 = '{}'.format(n.name)
            m1 = discord.utils.get(message.server.members, name="{}".format(n1))
            embed = discord.Embed(
                title="Sorteiar membro",
                colour=0xab00fd,
                description="Membro sorteado foi {}".format(m1.mention)
            )
            hh = await client.send_message(message.channel, "{}".format(m1.mention))
            await client.delete_message(hh)
            await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message(
                "{} você não tem permissão de executar esse comando!".format(message.author.mention))
    #------------------------------Verificar se e humano------------------------------
    #------------------------------FIM Dos Comandos---------------------------------==

    #-------------------------------Parte De Musica-------------------------------------


    #------------------------------------------Fim Da Parte de Musica--------------------------------------------


    if message.content.lower().startswith(".comandos"):
     comandos =discord.Embed(
        title="Lista de Comandos!",
        color=COMANDOS,
        description="**.ship** (@player1) (@player2) - Junta o Nome dos 2 Mencionados \n"
                    "**.gif** - Mostra um Gif Aleatorio\n"
                    "**.limpar** (Qtd) - Limpa a Qtd de Mensagens Que Você Pediu!\n"
                    "**.avatar** (@player) - Mostra o Avatar da Pessoa Que Você Mencionou\n"
                    "**.site** - Mostra o Endereço do Site Oficial\n"
                    "**.ts3** - Mostra o Ip Do Ts3 Do Team DxD\n"
                    "**.info** (@player) - Mostra Informaçoes da Pessoa Que Você Mencionou\n"
                    "**.jose** - Comando Personalizado Escolhido Pelo GuiihSouza_\n"
                    "**.serverinfo** - Mostra Informaçoes do Servidor\n"
                    "**.moeda** - Escolhe entre cara e coroa ",)

    botmsg = await client.send_message(message.author, embed=comandos)

    await client.send_message(message.channel, "Enviei As informaçoes no Seu Privado!")
    await client.add_reaction(message, "👍")
    await client.add_reaction(botmsg, "🇹")
    await client.add_reaction(botmsg, "🇴")
    await client.add_reaction(botmsg, "🇵")


    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author



client.run("NDU4NDY3NTY4OTExNTE1NjU5.DlmdJg.WaLSr5vVn4gh3imq9SdTHueL8K0")
