class Solution:
    def trap(self, height: List[int]) -> int:
        # water trap @ current idx = min(max bar on the left of idx, max bar on the right of ix) - height of bar at idx

        max_bar_left = []
        max_height = 0
        for i in range(len(height)):
            max_bar_left.append(max_height)
            max_height = max(max_height, height[i])
        
        max_bar_right = [0] * len(height)
        max_height = 0
        for i in range(len(height) - 1, -1 ,-1):
            max_bar_right[i] = max_height
            max_height = max(max_height, height[i])
        
        res = 0
        for i in range(len(height)):
            water = min(max_bar_left[i], max_bar_right[i]) - height[i]
            if water > 0:
                res += water
        return res
        