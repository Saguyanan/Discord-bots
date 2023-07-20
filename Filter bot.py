import discord
from random import randint
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
Client = discord.Client(intents=intents)
TOKEN = 'MTEyODQxMjk4Mjk0NzM1NjczMg.GJ87Lp.w_-7gGgZS_DB5WDIChMVOUPiRYb6gNP0451HtE'
Black_list = ['maple bitch', 'rope bunny', 'bark', 'woof','growl','whine', 'step on me']
Admin_list = ['saguya']
Filter_list = ['[Alex is deprived]','[Nathan is hot]']

@Client.event
async def on_message(message):
    if message.author == Client.user:
        return
    global username
    Filtercon = False
    username = str(message.author)
    user_message = str(message.content)
    user_message = user_message.lower()
    channel = str(message.channel.name)
    if username == 'karmakrl':
        Num = randint(1, 30)
        if Num == 15:
            await message.channel.send('stfu Gabby, Nathan is hotter')
    if message.content.startswith('!'):
        await message.channel.send(Commands(username, user_message))
        print(Black_list)
        return
    for word in Black_list:
        if word in user_message or word.replace(' ','') in user_message:
            Filtercon = True
    for word in user_message.split():
        print(word)
        if word in Black_list:
            Filtercon = True    
    if Filtercon:
        await message.delete()
        await message.channel.send(Filter(user_message))    
    print(f'{username}: {user_message} in {channel}')    


def Filter(Message):
    global username
    for word in Black_list:
        if word in Message or word.replace(' ','') in Message:
           Message = Message.replace(word, Filter_list[randint(0,1)])
           Message = Message.replace(word.replace(' ', ''), Filter_list[randint(0,1)])
    Split_message = Message.split()
    for Num, word in enumerate(Split_message):
        if word in Black_list:
            Split_message[Num] = Filter_list[randint(0,1)]
    Split_message = ' '.join(Split_message)                
    return str(username + ' meant to say: ' + Split_message)        


def Commands(Username,Message):
    Message = Message.replace(' ', '')
    if Username not in Admin_list:
        return(f'{Username} Not admin') 
    if '!bl'in Message:
        if Message[3:] != '':
            Black_list.append(Message[3:])
            return('Added')
        return('Word not specified')
    if '!wl' in Message:
        try:
            Black_list.remove(Message[3:])
            return('Removed')
        except:
            return('Word not in list')        
    return('Invalid command')            


@Client.event
async def on_ready():
    print('Running')    


Client.run(TOKEN)