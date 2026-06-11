class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res = res + str(len(word)) + '#' + word
        return res

    def decode(self, s: str):
        res, index, endIndex = [], 0, 0
        
        while index < len(s):
            while s[endIndex] != '#':
                endIndex+=1
            wordLen = int(s[index:endIndex])
            word = s[endIndex+1:endIndex+1 + wordLen]
            res.append(word)
            index = endIndex+1 + wordLen
            endIndex =  endIndex+1 + wordLen
        
        return res
             
    