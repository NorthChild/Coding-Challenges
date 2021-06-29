# Create a function that receives an array of numbers and returns an array containing only the positive numbers

mixedArray = [12, -34, -2, 54, 87, 99, -1, 45, -12, 21, 54, -42]

positiveArray = []
negativeArray = []

for i in mixedArray:
    if i > 0:
        positiveArray.append(i)
    else:
        negativeArray.append(i)

print(positiveArray)
