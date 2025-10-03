def isValidSudoku(board):

    flag = True
    def is_cond1(index):
        """condition to check if the row and col is valid"""
        row = {}
        col = {}

        # traverse through row
        for i in range(len(board)):
            row[board[i][index]] = row.get(board[i][index] , 0) + 1
            col[board[index][i]] = col.get(board[index][i], 0) + 1

        for i,j in list(zip(row.values() , col.values())):
            if i > 1 or j > 1:
                flag = False
                return

    def is_cond2(index):
        """condition to check if the box is valid or not"""
        arr = [0] * 9 
        for i in range(3):
            for j in range(3):
                if arr[board[index + i][index + j]] > 0:
                    flag = False
                    return
                else:
                    arr[board[index + i][index + j]] += 1
    
    # for loop for checking condition 1 and 2
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == j:
                is_cond1(i)
                if flag == False:
                    return False

    # for loop for checking condition 3
    for i in range(3):
        for j in range(3):
            board[i][j]
            i += 3
            j += 3


board = [
  ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
]


print(len(board))
