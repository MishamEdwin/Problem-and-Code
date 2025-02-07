board=[
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


def sudoku(board):
    # row validate
    for i in range(9):
        s = set()

        for j in range(9):
            element = board[i][j]

            if element in s:
                print("False")
                exit()
            elif element != ".":
                s.add(element)

        # print(s)

    # validate columns
    for i in range(9):
        s = set()

        for j in range(9):
            element = board[j][i]

            if element in s:
                print("False")
                exit()

            elif element != ".":
                s.add(element)

        #print(s)

    # validate boxes

    starts = [(0, 0), (0, 3), (0, 6),
              (3, 0), (3, 3), (3, 6),
              (6, 0), (6, 3), (6, 6)]

    for i, j in starts:
        s = set()

        for row in range(i, i + 3):  # i goes from (0 - 2)
            for col in range(j, j + 3):  # j goes from (0 - 2)
                item = board[row][col]

                if item in s:
                    print("False")
                    exit()
                elif item != ".":
                    s.add(item)

    print("True")

sudoku(board)


