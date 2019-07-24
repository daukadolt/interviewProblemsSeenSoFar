from typing import List, Set, Tuple

def isPalindrome(string: str) -> bool:
    iFront, iBack = 0, len(string)-1
    while iFront < iBack:
        front, back = string[iFront].lower(), string[iBack].lower()
        if not front.isalpha():
            iFront += 1
            continue
        if not back.isalpha():
            iBack -= 1
            continue
        if front == back:
            iFront += 1
            iBack -= 1
        else:
            return False
    return True

def countIslands(matrix: List[List[int]]) -> int:
    visited = set()
    numIslands = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not (x, y) in visited and matrix[y][x] == 1:
                recursivelyVisit(x, y, matrix, visited)
                numIslands += 1
    return numIslands

def recursivelyVisit(x: int, y: int, matrix: List[List[int]], visited: Set[Tuple[int]]) -> None:
    visited.add((x, y))
    for direction in [ [-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1] ]:
        deltaX, deltaY = direction
        i, j = (deltaX + x, deltaY + y)
        if i < 0 or i >= len(matrix[0]) or j < 0 or j >= len(matrix):
            continue
        if matrix[j][i] == 1 and not (i, j) in visited:
            recursivelyVisit(i, j, matrix, visited)