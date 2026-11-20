class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setA=set()
        setB=set()
        boxes = [set() for _ in range(9)]
        for i in range (9):
            setA.clear()
            setB.clear()
            for j in range(9):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in setA:
                    return False
                else:
                    setA.add(board[i][j])
                
                if board[j][i]== ".":
                    pass
                elif board[j][i] in setB:
                    return False
                else:
                    setB.add(board[j][i])
                val = board[i][j]
                if val != ".":
                    box_idx = (i // 3) * 3 + (j // 3)
                    if val in boxes[box_idx]:
                        return False
                    boxes[box_idx].add(val)
                
        return True
        