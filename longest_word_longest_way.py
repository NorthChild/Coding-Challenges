# Write a function giving the longest word in a given text.
# Your function should be named longest_word, take a single argument text and return a string which should be the longest word in the given text.

# SIDE NOTE: since we're looking for the longest word, we're gonna go the longest way, without using any method that could facilitate us (i.e len() etc.) 


def longest_word(text):
    list_of_words = text.split()
    values = []
    
    for i in list_of_words:
        count = 0
        for j in i:
            count += 1
    
        values.append(count)
    
    ord_list = sorted(values)
    biggest_n = ord_list[-1]

    pos = 0
    
    for x in values:
        if x == biggest_n:
            break
        else:
            pos += 1
    
    return list_of_words[pos]
    

    
if __name__ == "__main__":
    print(longest_word("We want a SHRUBBERY"))
    
    
    
    
