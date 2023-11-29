import telebot

bot = telebot.TeleBot('6653633773:AAG6Qd_iLKDBe1Euv4EPfZA7Yymjls--9Do')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'С ДНЁМ СВЯТОГО ВАЛЕНТИНА!!!')


@bot.message_handler(commands=['data'])
def main(message):
    bot.send_message(message.chat.id, '14 февраля')


@bot.message_handler(commands=['country'])
def main(message):
    bot.send_message(message.chat.id, '*Древний Рим*', parse_mode='Markdown')


@bot.message_handler(commands=['fact'])
def main(message):
    bot.send_message(message.chat.id, 'В этот день в мире продаётся более 50000000 роз')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, '[Любовь](https://pastebin.com)', parse_mode='Markdown')


bot.infinity_polling()
