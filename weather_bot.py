import telebot
from main import main
from telebot import types
from auth_data import bot_token

bot=telebot.TeleBot(bot_token)
#This is simple commands, you can add more :)
commands="""
/help
/start
"""
    
def telegram_bot(bot_token):   
    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hey there, type in format <b>City,Country</b> or just <b>City</b> you're interested in and i'll show all information", parse_mode="html")

    @bot.message_handler(commands=['help'])
    def help_message(message):
        bot.send_message(message.chat.id,f"Available commands: {commands}")

# This Decorator recieves every message you've typed, and divides it into 2 parts : City, Country. Country can be empty
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        country=""
        city=""
        i=0
        for char in message.text:
            if char ==',':
                i=1
            if i==0:
                city=city+char
            else:
                country=country+char
        data=main(city,country)
        bot.send_message(message.chat.id,f"{data}", parse_mode="html")
        # bot.send_message(message.chat.id, "Something went wrong. Please type /help")
   
    bot.polling()
if __name__=='__main__':
    telegram_bot(bot_token)
