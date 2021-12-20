#importing required libraries
import discord
import os
import random
import requests


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
article_cse_id = os.environ['Article_cse_id']
bookpdf_cse_id = os.environ['BookPdf_cse_id']
cse_key = os.environ['cse_key']



async def getLink(topic,user):

    result=[]

    #The topic to be searched
    query = " ".join(topic.split()[1:])

    #Start page
    page = 1

    #Request Url
    if(topic.split()[0]=="$topic"):
        url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&start={}".format(cse_key,article_cse_id,query,page)
    elif(topic.split()[0]=="$book"):
        url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&start={}".format(cse_key,bookpdf_cse_id,query,page)

    #getting the data from the customized search engine
    data = requests.get(url).json()

    #getting the search result items
    search_items = data.get("items")

    for i,search_item in enumerate(search_items,start=1):
        link = search_item.get("link")
        result.append(link)
    
    await user.send("You can navigate to the following links: \n"+"\n\n".join(result))




async def fullfillWish(wish,user):
    WISH = " ".join(wish.split()[1:])
    if(WISH=="1" or WISH.lower()=="article links"):
        await user.send("Start Typing your topic to get the article link...")
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
    
    elif(message_content.startswith("$topic") or message_content.startswith("$book")):
        user = message.author
        await getLink(message_content,user)

        
        
  
client.run(my_secret)


