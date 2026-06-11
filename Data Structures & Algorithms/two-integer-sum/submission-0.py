class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        indexes = range(len(nums))
        for x in indexes:
            if mydict and nums[x] in mydict:
                return [mydict[nums[x]], x]
            
            diff = target - nums[x]
            mydict[diff] = x

        return []