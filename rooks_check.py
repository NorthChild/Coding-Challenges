# check a chess board (width and height are always consistant) to see if any tower have any possibility of attacking another tower
# return true if theres any tower thats in danger, false if no tower is in danger

board = [[0,1,0,0],
         [0,0,1,0],
         [0,0,0,0],
         [0,0,0,1]]


def boardCheck(instance):
    print('\nAre all towers safe ?')
    n = len(instance)

    for row_i in range(n):
        row_count = 0

        for col_i in range(n):
            row_count += instance[row_i][col_i]

        if row_count > 1:
            return False

    for col_i in range(n):
        col_count = 0

        for row_i in range(n):
            col_count += instance[row_i][col_i]

        if col_count > 1:
            return False

    return True



print(boardCheck(board))
