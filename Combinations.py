class Solution:
    def combine(n: int, k: int):
        cands = [i+1 for i in n]
        def cb(i=0, res=[]):
            if len(res) < k:
                res.append(cands[i])
                return cb(i=i+1,res=res)
            else:
                return res
        return cb