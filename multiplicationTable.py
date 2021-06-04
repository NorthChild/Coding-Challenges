# create a function that prints the first 10 results of the multiplication table of a given integer

def multiTable(numb):

    for i in range(11):
        # we multiply the iterator by the given integer
        res = i * numb
        # we print the result
        print(str(i) + ' x ' + str(numb) + ' = ' + str(res))


multiTable(9)
