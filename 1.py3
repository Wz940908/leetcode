class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        x={}
        for index,i in enumerate(nums):
            if target-i not in x:
                x[i]=index
            else: return[x[target-i],index]
