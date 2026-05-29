class Solution:
    def minElement(self, nums: List[int]) -> int:
        self.new = []
        for i in range(len(nums)):
            total = 0
            temp = str(nums[i])
            for i in range(len(temp)):
                total += int(temp[i])
            self.new.append(total)
        nums = self.new
        return min(nums)