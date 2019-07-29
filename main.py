#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from telegram import ReplyKeyboardMarkup
import requests
from fonAPI import FonApi
from time import gmtime, strftime
fon = FonApi('Token from fonApi')
update_id = None
m = None
n = None   
c = None
sr = None
ss = None
w = None
startmessage = None
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('Token')
    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1
    
def bitcoin():
    global m
    response=requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
    m=response.json()['data']['amount']
    print(str(m))
def sun():
    global sr
    global ss
    response=requests.get('https://api.sunrise-sunset.org/json?lat=35.6892&lng=51.3890&date=today')
    m=response.json()['results']['sunrise']
    n=response.json()['results']['sunset']
    lhsr=int(m[0])+4
    lmsr=int(m[2])*10+int(m[3])+30
    if lmsr>=60:
        lhsr=lhsr+1
        lmsr=lmsr%60
    sr=str(lhsr)+":"+str(lmsr)+":"+m[5]+m[6]+"\n"
    lhss=int(n[0])+4
    lmss=int(n[2])*10+int(n[3])+30
    if lmss>=60:
        lhss=lhss+1
        lmss=lmss%60
    ss=str(lhss)+":"+str(lmss)+":"+n[5]+n[6]
def tehtemp():
    global n
    global c
    response=requests.get('https://api.darksky.net/forecast/dc0c0f77970a5bbac11a0b27d87fa51f/35.6892,51.3890')
    n=response.json()['currently']['temperature']
    c = int ((n-32)/1.8)
    print(str(c))
def start():
    global startmessage
    startmessage = "به دنیای تندرستی خوش آمدید." 
def openfda():
    global w
    response=requests.get('https://api.fda.gov/drug/enforcement.json?search=report_date:[20190101+TO+20190630]&limit=1')
    m=response.json()['results']
    n=(m[0])
    b="Product description: "+n['product_description']+"\n"
    c="Country: "+n['country']+"\n"
    d="City: "+n['city']+"\n"
    e="Center classification date: "+n['center_classification_date']+"\n"
    f="Classification: "+n['classification']+"\n"
    g="Code info: "+n['code_info']+"\n"
    h="Distribution pattern: "+n['distribution_pattern']+"\n"
    i="Event id: "+n['event_id']+"\n"
    j="Initial firm notification: "+n['initial_firm_notification']+"\n"
    k="Product quantity: "+n['product_quantity']+"\n"
    l="Product type: "+n['product_type']+"\n"
    o="Reason for recall: "+n['reason_for_recall']+"\n"
    p="Recall initiation date: "+n['recall_initiation_date']+"\n"
    q="Recall number: "+n['recall_number']+"\n"
    r="Recalling firm: "+n['recalling_firm']+"\n"
    s="Report date: "+n['report_date']+"\n"
    t="State: "+n['state']+"\n"
    u="Status: "+n['status']+"\n"
    v="Voluntary mandated: "+n['voluntary_mandated']+"\n"
    w=b+c+d+e+f+g+h+i+j+k+l+o+p+q+r+s+t+u+v
    print (b,c,d,e,f,g,h,i,j,k,l,o,p,q,r,s,t,u,v)

def device ():
    bot = telegram.Bot('Token')
    f = bot.get_updates()[0]
    device=f['message']['text']
    chat_id=f['message']['chat']['id']
    print(f['message']['chat']['username'],device,chat_id)
    phones = fon.getdevice(device)
    try:
        for phone in phones:
            a="Device name: "+phone['DeviceName']+"\n"
            b="Weight: "+phone['weight']+"\n"
            c="Resolution: "+phone['resolution']+"\n"
            d="Colors: "+phone['colors']+"\n"
            e="Primary camera: "+phone['primary_']+"\n"
            f="secondary camera: "+phone['secondary']+"\n"
            g="Dimensions: "+phone['dimensions']+"\n"
            h="Features: "+phone['features']+"\n"
            i="Sensors: "+phone['sensors']+"\n"
            j="CPU: "+phone['cpu']+"\n"
            k="Technology: "+phone['technology']+"\n"
            bot.send_message(chat_id, a+b+c+d+e+f+g+h+i+j+k)
    except:
        if bot.get_updates()[0]['message']['text']== "/start":
            print(bot.get_updates()[0]['message']['text'])
            bot.send_message(chat_id, "به دنیای تندرستی خوش آمدید.")
        elif bot.get_updates()[0]['message']['text']!= "/help":
            bot.send_message(chat_id,"روی یکی از دکمه های صفحه کلیک کنید.")
        elif bot.get_updates()[0]['message']['text']!= "/start":
            bot.send_message(chat_id,"روی یکی از دکمه های صفحه کلیک کنید.")
        elif bot.get_updates()[0]['message']['text']== "/help":
            bot.send_message(chat_id,"روی یکی از دکمه های صفحه کلیک کنید.")
        else:
            bot.send_message(chat_id, "گوشی مورد نظر پیدا نشد!")
        
def echo(bot):
    """Echo the message the user sent."""
    global n
    global c
    global m
    global update_id
    global startmessage
    CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

    reply_keyboard1 = [['قیمت بیت کوین', 'دمای کنونی تهران'],
                  ['طلوع و غروب خورشید', 'فراخوان استرداد دارویی'],
                  ['اطلاعات گوشی همراه']]
    
    markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=True)

    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            print (update.message)
            a = update.message.text
            if a=="قیمت بیت کوین":                
                bitcoin()
                update.message.reply_text(m, reply_markup=markup1)
            elif a=="دمای کنونی تهران":
                tehtemp()
                update.message.reply_text(c, reply_markup=markup1)
            elif a=="طلوع و غروب خورشید":
                sun()
                update.message.reply_text(" طلوع خورشید "+sr+" غروب خورشید "+ss, reply_markup=markup1)
            elif a=="فراخوان استرداد دارویی":
                openfda()
                update.message.reply_text(w, reply_markup=markup1)
            elif a=="اطلاعات گوشی همراه":
                update.message.reply_text( "لطفن مدل گوشی خود را به انگلیسی وارد کنید: ", reply_markup=markup1)
            else:
                device()

if __name__ == '__main__':
    main()
