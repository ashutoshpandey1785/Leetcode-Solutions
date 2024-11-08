class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        c1 = sorted(set(tasks))
        round = 0
        for i in c1:
            if c[i]<2:
                return -1
            else:
                round+=ceil(c[i]/3)
        return round