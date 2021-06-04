# Calculate the average of the numbers in an array of numbers

arr = [21, 23, 54, 65, 23, 0, -23, 65, 87, 123, 4578]
arrII = [12, 12, 0, -3, 65, 0, -9, 32, 5, -34, -92]
arrIII = [1, 2, 3]

def averageOfArray(array):

    sum = 0
    average = 0
    length = len(array)

    # we sum the contents of the array
    for i in array:
        sum += i
    # we devide the sum by the length of the array
    total = sum / length
    print('The Average of the Array is: ' + str(total))



averageOfArray(arr)
averageOfArray(arrII)
averageOfArray(arrIII)


