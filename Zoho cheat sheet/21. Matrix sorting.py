def main_func(mat):
    rows = len(mat)
    cols = len(mat[0])

    def diagonal_sort(start_row, start_col):
        diagonals = []
        r = start_row
        c = start_col

        # Extracting the diagonals
        while r < rows and c < cols:
            diagonals.append(mat[r][c])
            r += 1
            c += 1

        diagonals.sort()

        # Putting the diagonals back
        r = start_row
        c = start_col
        for values in diagonals:
            mat[r][c] = values
            r += 1
            c += 1

    # sort all the diagonals starting from first row
    for col in range(cols):
        diagonal_sort(0, col)
    # sort all the diagonals starting from first column
    for row in range(1, rows):
        diagonal_sort(row, 0)

    return mat


mat = [[3, 3, 1, 1],
       [2, 2, 1, 2],
       [1, 1, 1, 2]]

result = main_func(mat)

for ans in result:
    print(ans)



