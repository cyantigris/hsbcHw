def reverse_list(l: list):
    """
    TODO: Reverse a list without using any built in functions
    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    lenL = len(l)

    for i in range(0, int(lenL / 2)):
        tmp = l[i];
        l[i] = l[lenL - 1 - i]
        l[lenL - 1 - i] = tmp
    return l


# Test:
listTest = [1, 2, 3, "123", "A", ("c", "a")]
print(reverse_list(listTest))


def solve_sudoku(matrix):
    """
    TODO: Write a programme to solve 9x9 Sudoku board.
    Sudoku is one of the most popular puzzle games of all time.
    The goal of Sudoku is to fill a 9×9 grid with numbers so that each row,
    column and 3×3 section contain all of the digits between 1 and 9.
    As a logic puzzle, Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """
    def dfs(probe):
        nonlocal valid
        if probe == len(space):
            valid = True
            return

        i, j = space[probe]
        for digit in range(9):
            if row[i][digit] == col[j][digit] == block[i // 3][j // 3][digit] == False:
                row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = True
                matrix[i][j] = str(digit + 1)
                dfs(probe + 1)
                row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = False
            if valid:
                return

    row = [[False] * 9 for _ in range(9)]
    col = [[False] * 9 for _ in range(9)]
    block = [[[False] * 9 for _r in range(3)] for _c in range(3)]
    space = list()
    valid = False
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == '.':
                space.append((i, j))
            else:
                num = int(matrix[i][j]) - 1
                row[i][num] = col[j][num] = block[i // 3][j // 3][num] = True
    dfs(0)


matrixTest = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

solve_sudoku(matrixTest)
print(matrixTest)
