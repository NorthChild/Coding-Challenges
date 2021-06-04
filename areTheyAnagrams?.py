# check if two strings are anagrams
# example 1
x = 'Astronomer'
y = 'Moon starer'
# example 2
a = 'Astronomers'
c = 'Moon landing'
# example 3
d = 'Funeral'
c = 'Real Fun'

# split the strings and place them in a list
# order them alphabetically, if the first letter isnt a match, exit the function
# compare the two lists element by element


def anagramCheck(x, y):
    # first we standardize all letters in the lists by 'lower-casing' them
    x = x.lower()
    y = y.lower()

    # we then separate them and place them in a list
    firstString = list(x)
    secondString = list(y)

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
        print('The chosen words are anagrams')
    else:
        print('The chosen words are NOT anagrams')


# lets call the function to start checking 
anagramCheck(x, y)
anagramCheck(a, c)
anagramCheck(d, c)
