#Importing required libraries
import discord
import os
import random


#prints the discord library version installed on system
print(discord.__version__)


#Setting permissions for gateway intents 
#creating a connection to discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#Secret Token for Bot
my_secret = os.environ['TOKEN']

#Programmable Customized Search Engine Credentials
cse_id = os.environ['CSE_id']
cse_key = os.environ['CSE_key']


async def fullfillWish(wish,user):
    WISH = " ".join(wish.split()[1:])
    if(WISH=="1" or WISH.lower()=="article links"):
        await user.send("Start Typing your topic on which you would like to get the article link...")
        await user.send('Follow this syntax: \n$topic <topic to be searched>')
    elif(WISH=="2" or WISH.lower()=="pdf book links"):
        await user.send("Start typing your desired book name to get the download link....")
        await user.send('Follow this syntax: \n$book <book name>')


@client.event
async def on_ready():
    print("Successfully Connected to Discord")
    print("{} user logged in".format(client.user))


@client.event
async def on_member_join(member):

    msg_list = ["{} just joined the PARTY !!!","Hey {} , Welcome Onboard !!!","Hello {} , Did You bring a Pizza ???","{} slid into the server","Holaaaa {} !!!","You have successfully landed {} !!!"]

    channel = member.guild.get_channel(920641848148643883)

    await channel.send(random.choice(msg_list).format(member.name))


@client.event
async def on_message(message):
    message_content = message.content

    if("$DevBot" in message_content):
        await message.channel.send("Hey there {} . I am DevBot , How can I help you ???".format(message.author))

    elif("$features" in message_content):
        await message.channel.send('''Hello {} . Here's list to the things that I can do:
        1) [ Article Links
        2) Pdf Book Links
        3) Youtube Video Links ] on topics of technical domain
        4) Encouragement Quotes
        5) Chill Time Music'''.format(message.author))

    elif("$activate" in message_content):
        user = message.author

        await message.channel.send("Okay ... Shoot your wish {} in DM".format(message.author))

        await user.send("Hey buddy ! Let's get started...\nStart typing- $wish <followed by your wish from the list>")

    elif(message_content.startswith("$wish")):
        user = message.author
        await fullfillWish(message_content,user)
        
        
  
client.run(my_secret)


