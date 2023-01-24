import requests
import telebot
from telebot import types
import random
import os.path
import datetime
from datetime import datetime


def rename_files_to_numbers(path):
    number = 1
    for f in os.listdir(path):
        print(f)
        os.rename(path+'/'+f, f'{path}/.{number}.jpg')
        print(os.path)
        number += 1
    number = 1
    for f in os.listdir(path):
        print(f)
        os.rename(path+'/'+f, f'{path}/{number}.jpg')
        print(os.path)
        number += 1


def get_photo_search(name):
    page_number = random.randint(1, 10000)
    client_id_unsplash = 'XXXXXXXXXXXXXXXXXXXXXX' #There has to be your client_id from unsplash
    response = requests.get(f"https://api.unsplash.com/search/photos/?client_id={client_id_unsplash}&query={name}&per_page=1&page={page_number}")
    print(response.status_code)
    if response.status_code != 200:
        return "0"
    else:
        response_json = response.json()
        return response_json["results"][0]["urls"]["full"]


def get_compliment():
    response = requests.get("https://complimentr.com/api")
    response_json = response.json()
    compliment = response_json["compliment"]
    return compliment


def get_file_num(path):
    count_img = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    number = random.randint(1, count_img)
    return str(number)+'.jpg'

bot = telebot.TeleBot('XXXXXXXXXXXXXXXX') #there has to be your tgbot token from @BotFather
CHANNEL_NAME = "@XXXXX" #name of your bot
USERS = [] #list of user's telegram id, only they will have access to the bot

@bot.message_handler(commands=['start'])
def start_message(message):
    print(str(message.chat.id)+" "+str(datetime.now()))
    if message.chat.id not in USERS:
        bot.send_message(message.chat.id, "This chat isn't for you")
        return
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("What am i?")
    item2 = types.KeyboardButton("How are you?")
    item3 = types.KeyboardButton("Need your photo")
    item4 = types.KeyboardButton("I want to see an incredible sunset")
    item5 = types.KeyboardButton("I want to see a cute kitten")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Hello, ma girl', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.chat.id not in USERS:
        bot.send_message(message.chat.id, "This chat isn't for you")
        return

    if message.text == "How are you?":
        bot.send_message(message.chat.id, "I'm fine, and you?")
        return

    if message.text == "What am i?":
        compliment = get_compliment()
        file = get_file_num('./herimages')
        path = './herimages/'+file
        image = open(path,'rb')
        bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, compliment)
        print(message.chat.id)

    if message.text == "Need your photo":
        file = get_file_num('./myimages')
        path = './myimages/' + file
        image = open(path, 'rb')
        bot.send_photo(message.chat.id, image)
        print(message.chat.id)

    if message.text == "I want to see an incredible sunset":
        link = get_photo_search("sunset")
        print(link)
        if link == "0":
            bot.send_message(message.chat.id, "Not now babe(")
        else:
            bot.send_message(message.chat.id, link)
            bot.send_photo(message.chat.id, link)

    if message.text == "I want to see a cute kitten":
        link = get_photo_search("cute cat")
        print(link)
        if link == "0":
            bot.send_message(message.chat.id, "Not now babe(")
        else:
            bot.send_message(message.chat.id, link)
            bot.send_photo(message.chat.id, link)


bot.infinity_polling()