import telebot
from telebot.types import Message

TOKEN = '673902439:AAHqoHl3Ny-pTOIe179QmJVHuX1dqPo0Hf4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет!')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Я ничего не умею :(')

@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())

bot.polling()