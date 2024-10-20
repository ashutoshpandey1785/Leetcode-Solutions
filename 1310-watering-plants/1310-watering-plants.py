class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans, water = 0, capacity
        for i in range(len(plants)):
            if water < plants[i]:
                ans += (2 * i)
                water = capacity
            ans += 1
            water -= plants[i]
        return ans