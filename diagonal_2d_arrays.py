# print the diagonal sum of a given 2d array
# the 2d array will always have equal n of rows and column

# test the function with these
list2 = [[36,2,4],
        [4,4,7],
        [3,5,2]]

list3 = [[233,1,2],
        [0,150,2],
        [1,2,283]]

list4 = [[58,0],
         [0,11]]

list5 = [[390,1,2],
        [0,15,2],
        [1,2,15]]

list6 = [[20,0],
         [0,3]]

list7 = [[5,1,2,23],
          [0,15,2,12],
          [1,2,10,54],
          [11,23,5,0]]

# here we go with the function
def diagCounter(list):

    # see how many rows it has
    # based on its len we base our code
    val_of_list = len(list)
    # print('H of 2d array:',val_of_list)
    # how many containers for the diagonal values
    j = 0
    for j in range(val_of_list):
        elements = []

    # how many elements have to appended
    i = 0
    for i in range(val_of_list):
        elements.append(list[i][i])
        i += 1

    # measure the contents of the diagonal values
    total = 0
    for i in elements:
        total += i
        # print(i, end=" ")

    print('-> Diagonal Sum: ', total)


# try different lists, i've commented some print statements that can give you more info about the operations etc  

diagCounter(list2)
# diagCounter(list3)
# diagCounter(list4)
# diagCounter(list5)
# diagCounter(list6)
# diagCounter(list7)
