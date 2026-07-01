def kilograms_conversion(number, unit):
    """Convet kilograms to units"""

    #Convert kilograms to grams
    if unit == 'grams':
        answer = number * 1000

    #Convert kilograms to milligrams
    elif unit == 'milligrams':
        answer = number * 1000000

    #Convert kilograms to kilograms
    elif unit == 'kilograms':
        answer = number

    return answer

def grams_conversion(number, unit):
    """Convert grams to units"""

    #Convert grams to kilograms
    if unit == 'kilograms':
        answer = number * 0.001

    #Convert grams to milligrams
    elif unit == 'milligrams':
        answer = number * 1000

    #Convert grams to grams
    elif unit == 'grams':
        answer = number

    return answer

def milligrams_conversion(number, unit):
    """Convert milligrams to units"""

    #Covert millograms to kilograms
    if unit == 'kilograms':
        answer = number * 0.000001

    #Convert milligrams to grams
    elif unit == 'grams':
        answer = number * 0.001

    #Convert milligrams to milligrams
    elif unit == 'milligrams':
        answer = number

    return answer