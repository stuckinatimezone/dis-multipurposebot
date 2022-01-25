import discord
from discord.ext import commands, tasks
from datetime import datetime 
import random 
from random import choice
import time

client = discord.Client()
client = commands.Bot(command_prefix = "$")

#status code
status = ['Sleeping', 'Eating', 'with 100 people', 'on 7 different servers', 'Death chambers', 'squidgame', 
         'kahoot', 'with han', 'soccer', 'brushing']
#status code ends here

@client.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def tm(ctx):
   tm=time.strftime("%I:%M %p")
   await ctx.send((f'The time is:',tm))

@client.command(aliases=['8ball','lucky'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                'Without a doubt',
                'You may rely on it',
                'Yes definitely',
                'It is decidedly so',
                'As I see it, yes',
                'Most likely',
                'Yes',
                'Outlook good',
                'Signs point to yes',
                'Reply hazy try again',
                'Better not tell you now',
                'Ask again later',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don’t count on it',
                'Outlook not so good',
                'My sources say no',
                'Very doubtful',
                'My reply is no']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#classroom links code

@client.command(aliases=['ms','lnkms'])
async def links_1(ctx):
    await ctx.send(f'Your MS class/lab link...\n https://meet.google.com/qod-zktd-kgn')

@client.command(aliases=['cads'])
async def links_2(ctx):
    await ctx.send(f'Your CADS class link...\n https://meet.google.com/lookup/d42xiknccb')

@client.command(aliases=['cadslab'])
async def links_3(ctx):
    await ctx.send(f'Your CADS lab link...\n https://meet.google.com/lookup/bkrayxzjv3')

@client.command(aliases=['ca','CA'])
async def links_4(ctx):
    await ctx.send(f'Your CA link...\n https://meet.google.com/lookup/huvwuzx3vm')

@client.command(aliases=['os','OS'])
async def links_5(ctx):
    await ctx.send(f'Your OS link...\n https://meet.google.com/xcu-qfrj-acb')

@client.command(aliases=['oslab','OSlab','os lab','OS LAB','OS lab','Os lab','Os Lab','OSLAB'])
async def links_6(ctx):
    await ctx.send(f'Your OS LAB link...\n https://meet.google.com/nim-ewdo-niz')

@client.command(aliases=['DLD', 'dld'])
async def links_7(ctx):
    await ctx.send(f'Your DLD class link...\n https://meet.google.com/wkk-trbt-ikk')

@client.command(aliases=['DLDLAB', 'DLD lab', 'dldlab', 'dld lab', 'DLDlab', 'Dldlab'])
async def links_8(ctx):
    await ctx.send(f'Your DLD LAB link...\n https://meet.google.com/ppv-zfvw-bnz')

@client.command(aliases=['SEM','sem'])
async def links_9(ctx):
    await ctx.send(f'Your SEM class link...\n https://meet.google.com/eqh-cgfa-dzy')

@client.command(aliases=['SEM lab','SEMLAB','semlab','SEM LAB','sem lab'])
async def links_10(ctx):
    await ctx.send(f'Your SEM LAB link...\n https://meet.google.com/ozb-rvon-riw')

@client.command(aliases=['mc','MC'])
async def links_11(ctx):
    await ctx.send(f'Your Mandatory Course link...\n https://meet.google.com/lookup/e5iph6l4hb')

#classroom link code ends here.

#rock paper scissor implementation code begins from here...

@client.command(aliases=['play'])
async def rps(ctx, message):
    answer = message.lower()
    choices = ["rock", "paper", "scissors"]
    computer_answer = random.choice(choices)
    if answer not in choices:
        await ctx.send("That is not a valid option! Please use one of these options: rock, paper, scissors")
        return
    else:
        if computer_answer == answer:
            await ctx.send(f"Tie! We both picked {answer}")
        if computer_answer == "rock":
            if answer == "paper":
                await ctx.send(f"You win I picked {computer_answer} and you picked {answer}!")
        if computer_answer == "paper":
            if answer == "rock":
                await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")
        if computer_answer == "scissors":
            if answer == "rock":
                await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
        if computer_answer == "rock":
            if answer == "scissors":
                await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")
        if computer_answer == "paper":
            if answer == "scissors":
                await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
        if computer_answer == "scissors":
            if answer == "paper":
                await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")

#rock paper scissor implementation code ends here.

#the below code is to change status time limit for the status code at the starting of this coding
@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
#status loop code ends here

client.run('ODkxNDMxMDg4NTk2MDgyNzQ4.YU-P5Q.6SpwW_EBtJu5l8rSfVH1calFN9U')