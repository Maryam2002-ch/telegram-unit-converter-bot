def meters_conversion(number, unit):
    """تبدیل متر به واحدهای دیگر"""
    
    #تبدیل متر به سانتی متر
    if unit == 'سانتی متر':
        answer = number * 100

    #تبدیل متر به میلی متر
    elif unit == 'میلی متر':
        answer = number * 1000

    #تبدیل متر به میکرومتر
    elif unit == 'میکرومتر':
        answer = number * 1000000

    #تبدیل متر به متر
    elif unit == 'متر':
        answer = number

    return answer

def centimeters_conversion(number, unit):
    """تبدیل سانتی متر به واحدهای دیگر"""

    #تبدیل سانتی متر به متر
    if unit == 'متر':
        answer = number / 100

    #تبدیل سانتی متر به میلی متر
    elif unit == 'میلی متر':
        answer = number * 10

    #تبدیل سانتی متر به میکرومتر
    elif unit == 'میکرومتر':
        answer = number * 10000

    #تبدیل سانتی متر به سانتی متر
    elif unit == 'سانتی متر':
        answer == number

    return answer

def millimeters_conversion(number, unit):
    """تبدیل میلی متر به واحدهای دیگر"""

    #تبدیل میلی متر به متر
    if unit == 'متر':
        answer = number * 0.001

    #تبدیل میلی متر به سانتی متر
    elif unit == 'سانتی متر':
        answer = number * 0.1

    #تبدیل میلی متر به میکرومتر
    elif unit == 'میکرومتر':
        answer = number * 1000

    #تبدیل میلی متر به میلی متر
    elif unit == 'میلی متر':
        answer = number

    return answer

def micrometers_conversion(number, unit):
    """تبدیل میکرومتر به واحدهای دیگر"""

    #تبدیل میکرومتر به متر
    if unit == 'متر':
        answer = number * 0.000001

    #تبدیل میکرومتر به سانتی متر
    elif unit == 'سانتی متر':
        answer = number * 0.0001

    #تبدیل میکرومتر به میلی متر
    elif unit == 'میلی متر':
        answer = number * 0.001

    #تبدیل میکرومتر به میکرومتر
    elif unit == 'micrometers':
        answer = number

    return answer



