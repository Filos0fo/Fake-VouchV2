import requests
import os
import asyncio
import discord
import discordwebhook
from discord import Webhook
from discord_webhook import DiscordWebhook
import discord_webhook
import time
import random
import aiohttp
import json

url = "YOUR WEBHOOK HERE"

class FakeVouch:
    def __init__(self):

        self.webhook1 = open("config.txt" , "r").read()
        self.num_requests = int(input('How many requests do you want to send? '))
        self.use_delay = input('Use delay? (y/n) ').lower() == 'y'
        



        user_list = ['wimp', 'apron', 'lure', 'holystone', 'wealthy', 'alert', 'terrible', 'kindly', 'colt', 'heritage', 'deliver', 'income', 'plunk', 'awed', 'total', 'anybody', 'temporary', 'raven', 'stick', 'enjoin', 'frighten', 'excuse', 'hunt', 'kettle', 'tea', 'converting', 'kneel', 'ericsson', 'bracelet', 'bazaar', 'pitch', 'promotion', 'pplover', 'weekend', 'browtf', 'sugary', 'hazmat', 'honeycomb', 'waffle', 'magistrate', 'strip', 'winning', 'ribbon', 'cete', 's!r?outs', 'upon', 'growth', 'mute', 'cheerful', 'employer', 'normally', 'rinse', 'fe.e', 'cyclist', 'thorns75', 'fez', 'coati', 'hyena', 'trite', 'mercurial', 'wildebeest', 'garment', 'aberrant', 'enormous', 'celebrity', 'grass', 'peaceful', 'threat', 'ship', 'shooting', 'flowerpot', 'emotion', 'below33', 'attract', 'horseradish', 'undershirt']
        reason_list =  ['160k robux','10k robux','middleman','middleman a trade','500 robux ', 'sold me a cheap account', 'money maker fr', 'W', 'i love you ', '120$ usd middleman','middle man 100%','W mans fr',' vbucks method', 'spotify method']
        pfp_list = ['https://media.discordapp.net/attachments/1003495706096566292/1008342052800561172/IMG_0632.jpg?width=431&height=439','https://media.discordapp.net/attachments/941719216564895824/982160044961464330/IMG_8081.jpg?width=314&height=558','https://media.discordapp.net/attachments/932643101653205042/981302072135786576/akiyama_mio_k_on_drawn_by_tansuke__e47b156c8369fb9ec343893ca4025e7b.jpg?width=584&height=559','https://media.discordapp.net/attachments/941998018687803392/950431166454976512/33c61a47c39596ce2931b74a0fc15fe7.jpg?width=390&height=390','https://media.discordapp.net/attachments/941998018687803392/950431855423914034/d62e2b8ca1eb16341fb693a1840aeb69.jpg?width=378&height=378','https://media.discordapp.net/attachments/941719215600197722/982964599743713290/9FD84EE9-1E16-402F-B4E1-CDB1A00007B6.gif?width=540&height=540','https://media.discordapp.net/attachments/941997997363961868/954322865044488192/b7d0e353e4d4229e51e6fdc5d2f7a4b8.jpg?width=559&height=559','https://media.discordapp.net/attachments/1040478127715004498/1042116796414705794/48BE37A2-3857-46AC-861C-186F566F9F02.gif?width=266&height=265','https://media.discordapp.net/attachments/845429189972852767/1025207826873864243/79f65773071c321c47d76402e3654b0b.gif?width=270&height=270']
        
        co = 0
        
        while co < self.num_requests:

             user = random.shuffle(user_list)
             reason = random.shuffle(reason_list)
             pfp = random.shuffle(pfp_list)

             for user , reason, pfp in zip(user_list, reason_list, pfp_list):
                delay = random.randint(1, 3) if self.use_delay else 0 == "y"

                if delay > 0:
                    print('Sleeping for {delay} seconds...')
                    time.sleep(delay)
                    try:
                       
                         message= '+vouch <@1174438143529844812> ' + reason
                         url= 'https://discord.com/api/webhooks/1187838943966793858/xCvT_s9NvULitXIxX22HmCcspkE7nObuSFGR3XfNhboYjGIREoKa3GLG-oOlCDYxzjXN'
                         usern = user 
                         avatarurl = pfp
                         allowed_mentions= {
                             'user' : ['1174438143529844812']
                         }
                         webhook = DiscordWebhook(url=url, content=message, username=usern, avatar_url=avatarurl, allowed_mentions=allowed_mentions)
                         response = webhook.execute()
                
                         co += 1
                         print(f'Sent request {co}/{self.num_requests}')

                         time.sleep(delay)
                    except Exception as EnvironmentError:
                        print(f'Error')
                        continue

    def new_method(self):
        webhook1 = open("config.txt" , "r")
        return webhook1

if __name__ == '__main__':
    FakeVouch()
    url = "'https://discord.com/api/webhooks/1187838943966793858/xCvT_s9NvULitXIxX22HmCcspkE7nObuSFGR3XfNhboYjGIREoKa3GLG-oOlCDYxzjXN"


