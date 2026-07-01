import telebot
from length_unit_conversion import *
from weight_unit_conversion import *
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('token')

bot = telebot.TeleBot(token=token)

guide = "<i><b>Guide</b></i>\nSend your request in this format: \n10 meters to centimeters (from unit to unit)\n"
guide += "\nFor example: \n20 centimeters to meters.✅\n\n ⬇️Here are units that I can convert:\n"
guide += "\nLength unit convert : \ncentimeters, meters, millimeters, micrometers\n"
guide += "\nWeight unit convert : \nkilograms, grams, milligrams\n"
guide += "\n<i><b>Tips</b></i>\nIf you want to see the guide again, Please send /guide command.\n"
guide += "\nPlease send the units as shown below:\nmeters\ncentimeters\nmillimeters\nmicrometers\n"
guide += "kilograms\ngrams\nmilligrams\n"
guide += "\n❌Don't send units to convert that are not compatible!\n"

@bot.message_handler(commands=['start'])
def introduce_bot(message):
    """Robot introduces himself"""
    bot.send_message(chat_id=message.chat.id, text="Hello my friend👋! I'm a Unit Conversion bot. See the guide that I sending for you.")

    bot.send_message(chat_id=message.chat.id, text=guide, parse_mode='HTML')

@bot.message_handler(commands=['guide'])
def send_guide(message):
    """Send guide to user"""
    bot.reply_to(message=message, text=guide, parse_mode='HTML')

@bot.message_handler(func=lambda msg:True)
def unit_convert(message):
    """converting units"""
    parts = message.text.split()

    try:
        number = float(parts[0])

        f_unit = parts[1].lower() #from unit
        t_unit = parts[3].lower() #to unit

        #Length uint convert
        if f_unit == 'meters':
            answer = meters_conversion(number, t_unit)
        elif f_unit == 'centimeters':
            answer = centimeters_conversion(number, t_unit)
        elif f_unit == 'millimeters':
            answer = millimeters_conversion(number, t_unit)
        elif f_unit == 'micrometers':
            answer = micrometers_conversion(number, t_unit)

        #Weight unit convert
        if f_unit == 'kilograms':
            answer = kilograms_conversion(number, t_unit)
        elif f_unit == 'grams':
            answer = grams_conversion(number, t_unit)
        elif f_unit == 'milligrams':
            answer = milligrams_conversion(number, t_unit)

        #To better display the answer
        if number.is_integer() and answer.is_integer():
            number = int(number)
            answer = int(answer)

        bot.reply_to(message=message, text=f"✅{number} {f_unit} = {answer} {t_unit}")

    except ValueError:
        text = "❌Please send your request in right foramt(1 meters to centimeters).\n"
        text += "Send /guide command to see the guide "
        bot.reply_to(message=message, text=text)

    #When user sends uncompatible units conversion
    except UnboundLocalError:
        bot.reply_to(message=message, text= "❌Please don't send units to convert that are not compatible!\nSend /guide command to see the guide.")
    
    except IndexError:
        pass

if __name__ == "__main__":
    bot.infinity_polling()