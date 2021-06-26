# Provide a script printing every possible pairs of two different letters.
# Only lower case, one pair per line, ordered alphabetically.
# Don't print pairs consisting of twice the same letter, such as 'aa', 'bb', etc...

import string
from string import ascii_lowercase

def pair_em_up(string):
    
    for i in string:
        
        for j in string:
            
            if (i != j):
                print(f"{i}{j}")
    

pair_em_up(string.ascii_lowercase)
