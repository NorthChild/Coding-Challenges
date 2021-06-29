# Find the maximum number in an array of numbers

mixedArray = [12, -34, -2, 54, 87, 99, -1, 45, -12, 21, 54, -42]

def arrayChecker(array):

    highestNum = 0

    for i in mixedArray:
        if (i > highestNum):
            highestNum = i
    print(highestNum)


arrayChecker(mixedArray)
