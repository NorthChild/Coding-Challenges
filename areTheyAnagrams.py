# check if two strings are anagrams
# Example 1
# 'Astronomer'
# 'Moon starer'

# Example 2
# 'Flat earthers'
# 'make me feel better about myself'

# Example 3
# 'Funeral'
# 'Real Fun'


def anagramCheck(one, two):
    # first we standardize all letters in the lists by 'lower-casing' them
    one = one.lower()
    two = two.lower()

    # we then separate them and place them in a list
    firstString = list(one)
    secondString = list(two)

    # we then sort them alphabetically
    sorted1st = sorted(firstString)
    sorted2nd = sorted(secondString)

    # we then remove possible empty spaces
    # for the first list
    for i in sorted1st:
        if i == ' ':
            sorted1st.remove(i)

    # for the second list
    for i in sorted2nd:
        if i == ' ':
            sorted2nd.remove(i)

    # then we check if the two lists are the same
    if (sorted1st == sorted2nd):
        print('The chosen words: (' + one.upper() + ') and (' + two.upper() + '), are Anagrams \n')
    else:
        print('The chosen words: (' + one.upper() + ') and (' + two.upper() + '), are NOT Anagrams \n')



# lets call the function to start checking
anagramCheck('Astronomer', 'Moon starer')
anagramCheck('Flat earthers', 'make me feel better about myself')
anagramCheck('Funeral', 'Real Fun')
