# create a function that sums the numbers from 1 to 100 (you can change the end number to whatever)

def ifGaussHadAComputerAndWasLazy(endNum):
    total = 0

    for i in range(1, endNum + 1):
        # as we go through the loop, the iterator adds up to the total
        total = total + i
        
    print(total)


ifGaussHadAComputerAndWasLazy(100)

