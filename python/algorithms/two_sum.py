class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            acc = target - nums[i]
            if acc in d:
                return [d[acc], i]
            else: d[nums[i]] = i
                
        return []
