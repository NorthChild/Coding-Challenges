# Calculate the sum of numbers in an array of numbers

arr = [21, 23, 54, 65, 23, 0, -23, 65, 87, 123, 4578]
arrII = [12, 12, 0, -3, 65, 0, -9, 32, 5, -34, -92]
arrIII = [1, 2, 3]

def calculateContentsOfArray(array):
    sum = 0
    for i in array:
        sum += i
    print('Sum of Array is: ' + str(sum))


calculateContentsOfArray(arr)
calculateContentsOfArray(arrII)
calculateContentsOfArray(arrIII)
