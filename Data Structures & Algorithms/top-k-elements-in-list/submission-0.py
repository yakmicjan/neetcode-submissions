class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countDict = {}
        bucketCount = {i:[] for i in range(1,len(nums) +1)}
        output = []


        for num in nums:
            countDict[num] = countDict.get(num, 0) + 1

        for key, value in countDict.items():
            bucketCount[value].append(key)

        for i in range(len(nums), 0, -1):
            for j in bucketCount[i]:
                output.append(j)
                if len(output) == k:
                    return output
                

