class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        n = len(dominoes)
        pair_count = {}
        for i in range(n):
            dom = dominoes[i]
            if (dom[0], dom[1]) in pair_count:
                pair_count[(dom[0], dom[1])] -= 1
                res += pair_count[(dom[0], dom[1])]
                continue
            if (dom[1], dom[0]) in pair_count:
                pair_count[(dom[1], dom[0])] -= 1
                res += pair_count[(dom[1], dom[0])]
                continue
            count = 0 
            for j in range(i + 1, n):
                first = dominoes[i]
                second = dominoes[j]
                if first[0] == second[0] and first[1] == second[1] or first[0] == second[1] and first[1] == second[0]:
                    count += 1
            pair_count[(dominoes[i][0], dominoes[i][1])] = count
            res += count
        return res


        