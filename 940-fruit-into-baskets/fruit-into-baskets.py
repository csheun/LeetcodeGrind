class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # find largest window with 2 different integer
        l = 0
        basket = {}
        max_fruit = 0
        for r in range(len(fruits)):
            fruit = fruits[r]
            if fruit in basket:
                basket[fruit] += 1
            else:
                if len(basket) == 2:
                    while len(basket) == 2:
                        basket[fruits[l]] -= 1
                        if basket[fruits[l]] == 0:
                            del basket[fruits[l]]
                        l += 1
                basket[fruit] = 1
            max_fruit = max(max_fruit, r - l + 1)
        
        return max_fruit
        