class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for k in range(len(nums)-1, -1, -1):
            left = 0
            right = k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left  # each l from (l, l+1,..., r-1) and r
                    right -= 1
                else:
                    left += 1

        return count