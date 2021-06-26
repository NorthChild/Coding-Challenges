# Provide a script printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically.

import string
from string import ascii_lowercase

def every_two_letters(string):
    
    for i in string:
        
        for y in string:
            print(i+y)
                
            
every_two_letters(string.ascii_lowercase)
