# create a function that converst Fahrenheit to Celsius
# T(°C) = (T(°F) - 32) × (5/9)

# create a function that converst Celsius to Fahrenheit
# T(°F) = T(°C) × 9/5 + 32

def sillyAmericanToEverybodyElse(value):
    result = (value - 32) * (5/9)
    print(str(value) + '˚ Fahrenheit = ' + str(round(result, 2)) + '˚ Celsius')


def everybodyElseToSillyAmerican(value):
    result = (value * 9/5) + 32
    print(str(value) + '˚ Celsius = ' + str(round(result, 2)) + '˚ Fahrenheit')


sillyAmericanToEverybodyElse(113)
everybodyElseToSillyAmerican(45)
