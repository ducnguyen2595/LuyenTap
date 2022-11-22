from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums) 
        self.ST = [-float("inf")] * (2*self.n)
        self.createST()
    def createST(self):
        for i in range(self.n, 2* self.n):
            self.ST[i] = self.nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            print(f"{i}  = {self.ST[2*i]} + {self.ST[2*i + 1]}")
            self.ST[i] = self.ST[2*i] + self.ST[2*i + 1]
        print(self.ST)
        
    def update(self, i: int, val: int) -> None:
        
        i += self.n
        if val == self.ST[i]:
            return
        # delta = val - self.ST[i]
        self.ST[i] = val
        while i > 0:
            l = i
            r = i
            if i % 2 == 0:
                r = i + 1
            else:
                l = i - 1
            i //= 2
            self.ST[i] = self.ST[l] + self.ST[r]
            
        # print(f"updated Tree {self.ST}")
        return

    def sumRange(self, left: int, right: int) -> int:
        
        left += self.n
        right += self.n
        print(f"sum from {left} - {right} n = {self.n} => {self.nums[left - self.n: right +1 - self.n]}")
        m = -float("inf")
        s = 0
        if left == right:
            return self.ST[right]
        
        while left <= right:
            if left % 2 == 1:
                print(f"include if left is odd {left}: {s} += {self.ST[left]} increase left to {left + 1}")
                s += self.ST[left]
                left += 1
            if right % 2 == 0:
                print(f"include if right is even {right}: {s} += {self.ST[right]} decrease to {right - 1} ")
                s += self.ST[right]
                right -= 1
            left //=2
            right //= 2
            print(f"new {left}-{right}")
        
        return s

# Your NumArray object will be instantiated and called as such:
nums = [8,2,3,4,5,6,7]
obj = NumArray(nums)
obj.update(2, 3)
print(obj.sumRange(0, 4))
print(obj.sumRange(1, 6))


