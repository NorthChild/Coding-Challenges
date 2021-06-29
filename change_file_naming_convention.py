# change file naming convention from camelCase to under_score

string1 = 'thisFileHasToChange.py'
string2 = 'thisFileAlso.py'
string3 = 'youKnowTheDeal.py'
string4 = 'yadaYadaYada.py'

def change_naming_convention(string):

    changed_string = ''

    for i in string:

        if i.isupper() == True:
            changed_string += f'_{i.lower()}'
        else:
            changed_string += i

    print(f"'{string}' becomes '{changed_string}'")


change_naming_convention(string1)
change_naming_convention(string2)
change_naming_convention(string3)
change_naming_convention(string4)
