def kilograms_conversion(number, unit):
    """Convet kilograms to units"""

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
    """Convert grams to units"""

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
    """Convert milligrams to units"""

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