def kilograms_conversion(number, unit):
    """تبدیل کیلوگرم به واحدهای دیگر"""

    #تبدیل کیلوگرم به گرم
    if unit == 'گرم':
        answer = number * 1000

    #تبدیل کیلوگرم به میلی گرم
    elif unit == 'میلی گرم':
        answer = number * 1000000

    #تبدیل کیلوگرم به کیلوگرم
    elif unit == 'کیلوگرم':
        answer = number

    return answer

def grams_conversion(number, unit):
    """تبدیل گرم به واحدهای دیگر"""

    #تبدیل گرم به کیلوگرم
    if unit == 'کیلوگرم':
        answer = number * 0.001

    #تبدیل گرم به میلی گرم
    elif unit == 'میلی گرم':
        answer = number * 1000

    #تبدیل گرم به گرم
    elif unit == 'گرم':
        answer = number

    return answer

def milligrams_conversion(number, unit):
    """تبدیل میلی گرم به واحد های دیگر"""

    #تبدیل میلی گرم به کیلوگرم
    if unit == 'کیلوگرم':
        answer = number * 0.000001

    #تبدیل میلی گرم به گرم
    elif unit == 'گرم':
        answer = number * 0.001

    #تبدیل میلی گرم به میلی گرم
    elif unit == 'میلی گرم':
        answer = number

    return answer