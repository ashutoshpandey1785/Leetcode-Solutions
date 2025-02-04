from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        m = max(weights)
        s = sum(weights)

        def rtrdays(weights, capacity):
            day = 1
            load = 0

            for weight in weights:
                if load + weight > capacity:
                    day += 1
                    load = 0
                load += weight

            return day

        def bs(weights, start, end, days):
            while start <= end:
                mid = (start + end) // 2
                if rtrdays(weights, mid) <= days:
                    end = mid - 1
                else:
                    start = mid + 1
            return start

        least_capacity = bs(weights, m, s, days)
        return least_capacity

