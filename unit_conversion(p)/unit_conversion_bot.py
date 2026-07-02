import telebot
from length_unit_conversion import *
from weight_unit_conversion import *
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('token')

bot = telebot.TeleBot(token=token)

guide = "<i><b>راهنما</b></i>\nدرخواست خود را به این شکل ارسال کنید: \n10 متر به سانتی متر (از یک واحد به واحد دیگر)\n"
guide += "\nمثال: \n20 سانتی متر به متر✅\n\n ⬇️در زیر، تعداد واحدهایی که میتوانم تبدیل کنم، آورده شده است:\n"
guide += "\nتبدیل واحدهای طول : \nمتر, سانتی متر, میلی متر, میکرومتر\n"
guide += "\nتبدیل واحدهای وزن : \nکیلوگرم, گرم, میلی گرم\n"
guide += "\n<i><b>نکات</b></i>\nبرای دیدن دوباره راهنما، لطفا دستور /راهنما را ارسال کنید.\n"
guide += "\nلطفا واحدها را دقیقا به شکل زیر ارسال کنید: \nمتر\nسانتی متر\nمیلی متر\nمیکرومتر"
guide += "\nکیلوگرم\nگرم\nمیلی گرم\n"
guide += "\n❌لطفا از ارسال واحدهای ناسازگار خودداری کنید!\n"

@bot.message_handler(commands=['start'])
def introduce_bot(message):
    """Robot introduces himself"""
    bot.send_message(chat_id=message.chat.id, text="سلام👋! من یک ربات تبدیل واحد هستم. لطفا به راهنمایی که ارسال شد، توجه کنید.")

    bot.send_message(chat_id=message.chat.id, text=guide, parse_mode='HTML')

@bot.message_handler(commands=['راهنما'])
def send_guide(message):
    """Send guide to user"""
    bot.reply_to(message=message, text=guide, parse_mode='HTML')

@bot.message_handler(func=lambda msg:True)
def unit_convert(message):
    """converting units"""
    parts = message.text.split("به")

    part1 = parts[0].strip()    #عدد + واحد مبدا
    part2 = parts[1].strip()      #واحد مقصد
    
     #جدا کردن عدد از واحد مبدا
    from_unit = part1.split()
    number = float(from_unit[0])
    from_unit = ' '.join(from_unit[1:])  

    #تعیین واحد مقصد
    to_unit = part2     
    
    try:
        
        #Length uint convert
        if from_unit == 'متر':
            answer = meters_conversion(number, to_unit)
        elif from_unit == 'سانتی متر':
            answer = centimeters_conversion(number, to_unit)
        elif from_unit == 'میلی متر':
            answer = millimeters_conversion(number, to_unit)
        elif from_unit == 'میکرومتر':
            answer = micrometers_conversion(number, to_unit)

        #Weight unit convert
        if from_unit == 'کیلوگرم':
            answer = kilograms_conversion(number, to_unit)
        elif from_unit == 'گرم':
            answer = grams_conversion(number, to_unit)
        elif from_unit == 'میلی گرم':
            answer = milligrams_conversion(number, to_unit)

        #To better display the answer
        if number.is_integer() and answer.is_integer():
            number = int(number)
            answer = int(answer)

        bot.reply_to(message=message, text=f"✅{number} {from_unit} = {answer} {to_unit}")

    except ValueError:
        text = "❌Please send your request in right foramt(1 meters to centimeters).\n"
        text += "Send /guide command to see the guide "
        bot.reply_to(message=message, text=text)

    #برای زمانی که کاربر ، تبدیل واحدهای ناسازگار ارسال کرد
    except UnboundLocalError:
        bot.reply_to(message=message, text= "❌Please don't send units to convert that are not compatible!\nSend /guide command to see the guide.")
    
    except IndexError:
        pass


bot.infinity_polling()