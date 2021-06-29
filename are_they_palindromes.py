# are the strings palindromes?

string1 = "noon"
string2 = "kayak"
string3 = "general"
string4 = "anna"
string5 = "Aibohphobia"


def palindrom_checker(string):

    for i in string:
        reverserd_word = string[::-1]

    if string == reverserd_word:
        print(f"\n{string} is indeed a palindrome \n")
    else:
        print(f"\n{string} is not a palindrome \n")


palindrom_checker(string1)
palindrom_checker(string2)
palindrom_checker(string3)
palindrom_checker(string4)
palindrom_checker(string5)
