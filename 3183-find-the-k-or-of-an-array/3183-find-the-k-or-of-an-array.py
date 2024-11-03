class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(32):
            count = 0
            n = 2**i
            for num in nums:
                if num & n:
                    count += 1
            if count >= k:
                res += n
        return res