class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        players.sort()
        trainers.sort()
        j = 0
        for i in range(len(players)):
            if (j >= len(trainers)):
                break
            while(trainers[j] < players[i]):
                j += 1
                if (j == len(trainers)):
                    return res
            j += 1           
            res += 1

        return res

        