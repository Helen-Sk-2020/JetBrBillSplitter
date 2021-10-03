def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    print(f'{round(temps_c, 2)} C')


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    print(f'{round(temps_f, 2)} F')


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    if unit == 'F':
        temps_f = float(temperature)
        fahrenheit_to_celsius(temps_f)
        
    elif unit == 'C':
        temps_c = float(temperature)
        celsius_to_fahrenheit(temps_c)
        
        
# II
# def fahrenheit_to_celsius(temps_f):
#     temps_c = (temps_f - 32) * 5 / 9
#     return round(temps_c, 2)
#
#
# def celsius_to_fahrenheit(temps_c):
#     temps_f = temps_c * 9 / 5 + 32
#     return round(temps_f, 2)
#
#
# def main():
#     """Entry point of the program."""
#     temperature, unit = input().split()  # read the input
#     temp = ""
#     if unit == 'F':
#         temp = fahrenheit_to_celsius(int(temperature))
#         print("{0} {1}".format(temp, 'C'))
#     else:
#         temp = celsius_to_fahrenheit(int(temperature))
#         print("{0} {1}".format(temp, 'F'))
        