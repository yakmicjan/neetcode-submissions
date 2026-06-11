class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictA = dict()
        dictB = dict()
        for x in s:
            if x not in dictA:
                dictA[x] = 1
            else:
                dictA[x]+=1
        for x in t:
            if x not in dictB:
                dictB[x] = 1
            else:
                dictB[x]+=1
        if dictA == dictB:
            return True 
        return False        