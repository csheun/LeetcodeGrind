class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # can flow into pacific if row = 0 or col = 0
        # can flow into atlantic if row = n - 1 or col = n - 1

        # expand from the set of cells that can flow into ocean to get the cells that can be reach
        # take insection of both

        # pacific
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        n_row = len(heights)
        n_col = len(heights[0])
        reach_pacific = set()
        queue = deque()
        for i in range(n_row):
            row = i
            col = 0
            reach_pacific.add((row, col))
            queue.append((row, col))
        for i in range(n_col):
            row = 0
            col = i
            reach_pacific.add((row, col))
            queue.append((row, col))
        print("Queue start: ", queue)
        while queue:
            x, y = queue.pop()
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < n_row and 0 <= new_y < n_col:
                    if heights[new_x][new_y] >= heights[x][y] and (new_x, new_y) not in reach_pacific:
                        queue.append((new_x, new_y))
                        reach_pacific.add((new_x, new_y))
        reach_atlantic = set()
        queue = deque()
        for i in range(n_row):
            row = i
            col = n_col - 1
            reach_atlantic.add((row, col))
            queue.append((row, col))
        for i in range(n_col):
            row = n_row - 1
            col = i
            reach_atlantic.add((row, col))
            queue.append((row, col))
        while queue:
            x, y = queue.pop()
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < n_row and 0 <= new_y < n_col:
                    if heights[new_x][new_y] >= heights[x][y] and (new_x, new_y) not in reach_atlantic:
                        queue.append((new_x, new_y))
                        reach_atlantic.add((new_x, new_y))
        intersect = reach_pacific & reach_atlantic

        return [list(x) for x in intersect]
                


        