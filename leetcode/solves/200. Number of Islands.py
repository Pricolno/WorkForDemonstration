class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_size = len(grid)
        m_size = len(grid[0])

        def can_go(x, y):
            nonlocal m_size, n_size
            return 0 <= x < m_size and 0 <= y < n_size

        go_vec = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        used = [[False for _ in range(m_size)]
            for _ in range(n_size)
        ]

        def dfs(x: int, y: int,
            used: list[list[[bool]]], grid: List[List[str]],
            go_vec: list[tuple[int, int]]
        ):
            used[y][x] = True
            for dx, dy in go_vec:
                to_x = x + dx
                to_y = y + dy
                if can_go(to_x, to_y) \
                    and grid[to_y][to_x] == "1" \
                    and not used[to_y][to_x]:
                    dfs(to_x, to_y, used, grid, go_vec)
            
            return 
        
        cnt_comp = 0
        for y_ind in range(n_size):
            for x_ind in range(m_size):
                if grid[y_ind][x_ind] == "0":
                    continue
                
                if not used[y_ind][x_ind]:
                    cnt_comp += 1
                    dfs(x_ind, y_ind, used, grid, go_vec)
        return cnt_comp
    
