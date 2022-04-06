"https://leetcode.com/problems/group-anagrams/"
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        popped = []
        if len(strs) == 1:
            res.append(strs)
            return res
        for i in range(len(strs)):
            s = strs[i]
            if s in popped and len(s) > 0: continue
            sLen = len(s)
            sLetters = [i for i in s]
            sLetterCounts = [sLetters.count(i) for i in sLetters]
            tmp = [s]
            popped.append(s)
            for j in strs[i+1::]:
                if j in popped: continue
                checkLetter = 0
                for k in s:
                    if k in j:
                        checkLetter+=1
                if checkLetter == sLen:
                    tmp.append(j)
                    popped.append(j)
            res.append(tmp)
        return res