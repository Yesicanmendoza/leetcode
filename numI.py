def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    from collections import deque
        
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def bfs(grid, r, c, visited):
        q = deque()            
        q.append((r,c))

        while q:
            r, c = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                row = r + dr
                col = c + dc
                #print(row, col)
                if grid[row][col]:
                    if (row, col) not in visited and grid[row][col] == '1':
                        visited.add((row, col))
                        q.append((row, col))
                        #print(row, col, grid[row][col])
                        #print(q)
                        #print()
              


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                visited.add((r, c))
                bfs(grid, r, c, visited)
                islands += 1
                #print(visited, islands)


    return islands


