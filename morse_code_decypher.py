# Decode a message

message = ['.--.', '-.--', '-', '....', '---', '-.', '/', '..', '...', '/', '..-.', '..-', '-.', '-.-.--']

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': '/',
        '!': '-.-.--',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

def decode_message(message):
    converted_message = ''

    for i in message:
        for key, value in CODE.items():
            if value == i:
                print(key)
                converted_message += key

    message = converted_message.lower()
    print(message)


decode_message(message)
