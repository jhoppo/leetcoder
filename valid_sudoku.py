"""
Runtime: 148 ms, faster than 39.27% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.8 MB, less than 87.02% of Python3 online submissions for Valid Sudoku.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkDup(l):
            return sum([l[i] in l[i+1:] and l[i]!="." if i < len(l) else False for i in range(len(l))])
        tboard = list(map(lambda x: list(map( lambda y:board[y][x], range(len(board[x])) )), range(len(board))))
        # check board
        checkb = sum([ checkDup(l=l) for l in board ])
        # check t-board
        checkt = sum([ checkDup(l=l) for l in tboard])
        # check square
        def sqrList(board=board):
            sList=[]
            for i in range(0,len(board),3):
                iLists = [i,i+1,i+2]
                for j in range(0,len(board),3):
                    jLists=[j,j+1,j+2]
                    sList.append([board[m][n] for m in iLists for n in jLists])
            return sList
        sboard = sqrList()
        checks = sum([ checkDup(l=l) for l in sboard])
        if checkb > 0 or checkt > 0 or checks > 0:
            return False
        else:
            return True