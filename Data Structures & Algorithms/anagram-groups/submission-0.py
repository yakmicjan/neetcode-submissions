class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = dict()
        output = []

        for i, word in enumerate(strs):
            sortedWord = "".join(sorted(word))
            if sortedWord not in anagramDict:
                anagramDict[sortedWord] = [strs[i]]
            else:
                anagramDict[sortedWord].append(strs[i])
            
        for key, value in anagramDict.items():
             output.append(value)
        
        return output