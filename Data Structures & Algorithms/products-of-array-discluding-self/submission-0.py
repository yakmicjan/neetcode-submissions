class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countZeros = 0
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                countZeros +=1
                continue         
            product *= nums[i]

        if countZeros == 0:
            res = [product] * len(nums)
        else:
            res = [0] * len(nums)
            

        for i in range(len(nums)):
            if(countZeros == 1 and nums[i] == 0):
                res[i] = product
            if(countZeros == 0):
                res[i] = int(res[i] / nums[i])
        
        return res