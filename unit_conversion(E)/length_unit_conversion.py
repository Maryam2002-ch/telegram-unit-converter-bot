def meters_conversion(number, unit):
    """Convert meters to units"""
    
    #Cnovert meters to centimeters
    if unit == 'centimeters':
        answer = number * 100

    #Convert meters to millimeters
    elif unit == 'millimeters':
        answer = number * 1000

    #Convert meters to micrometers
    elif unit == 'micrometers':
        answer = number * 1000000

    #Convert meters to meters
    elif unit == 'meters':
        answer = number

    return answer

def centimeters_conversion(number, unit):
    """Convert centimeters to units"""

    #Convert centimeters to meters
    if unit == 'meters':
        answer = number / 100

    #Convert centimeters to millimeters
    elif unit == 'millimeters':
        answer = number * 10

    #Cnovert centimeters to micrometers
    elif unit == 'micrometers':
        answer = number * 10000

    #Convert centimeters to centimeters
    elif unit == 'centimeters':
        answer = number

    return answer

def millimeters_conversion(number, unit):
    """Convert millimeters to units"""

    #Convert millimeters to meters
    if unit == 'meters':
        answer = number * 0.001

    #Convert millimeters to centimeters
    elif unit == 'centimeters':
        answer = number * 0.1

    #Convert millimeters to micrometers
    elif unit == 'micrometers':
        answer = number * 1000

    #Convert millimeters to millimeters
    elif unit == 'millimeters':
        answer = number

    return answer

def micrometers_conversion(number, unit):
    """Convert micrometers to units"""

    #Convert mictometers to meters
    if unit == 'meters':
        answer = number * 0.000001

    #Convert micrometers to centimeters
    elif unit == 'centimeters':
        answer = number * 0.0001

    #Convert micrometers to millimeters
    elif unit == 'millimeters':
        answer = number * 0.001

    #Convert micrometers to micrometers
    elif unit == 'micrometers':
        answer = number

    return answer

