class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(n):
            if len(n)<=1:
                return n
            l,m,r=[],[],[]
            pivot=random.choice(n)
            for i in n:
                if i==pivot:
                    m.append(i)
                elif i<pivot:
                    l.append(i)
                else:
                    r.append(i)
            return quicksort(l)+m+quicksort(r)
        return quicksort(nums)