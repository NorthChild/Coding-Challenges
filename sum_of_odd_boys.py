# Calculate the sum of odd numbers greater than 10 and less than 30 (or any other interval)

def sumTheOddBoisss(start, end):

    total = 0
    # we start the loop with the integer we want to start with
    for i in range(start, end + 1):
        # if the integer is odd, we add it to the total
        if i % 2 == 1:
            total += i
        i += 1

    print(total)

sumTheOddBoisss(10, 30)
# sumTheOddBoisss(23, 420)

