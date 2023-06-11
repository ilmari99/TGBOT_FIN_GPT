import random
from FinGPTelebot import FinGPTelebot

with open("_token.txt", "r") as f:
    TOKEN = f.read().strip()

MODEL_NAME = 'TurkuNLP/gpt3-finnish-large'
N_MESSAGES = 10
CHAT_TYPES = ['group', 'supergroup', 'private', 'channel', 'bot' ]
bot = FinGPTelebot(MODEL_NAME, TOKEN, N_MESSAGES, simulate_users = True)
@bot.bot.message_handler(commands=['start', 'help'], chat_types=CHAT_TYPES)
def give_info(message):
    bot.give_info(message.chat.id)

@bot.bot.message_handler(content_types=['sticker'], chat_types=CHAT_TYPES)
def sticker_input(message):
    bot.store_sticker(message)

@bot.bot.message_handler(content_types=['document'], chat_types=CHAT_TYPES)
def file_input(message):
    bot.store_file(message)


@bot.bot.message_handler(func=lambda message: True, content_types=['text'], chat_types=CHAT_TYPES)
def possibly_reply(message):
    bot.store_message(message)
    if random.random() < 0.5 or "gpt" in message.text.lower():
        bot.send_reply(message.chat.id)

bot.run()