# Definition for singly-linked list.
from functools import reduce
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []: return
        def ln2l(res: list,ln):
            if ln == None or ln == []:
                return
            else:
                res.append(ln.val)
                if ln.next == None:
                    return res
                else:
                    return ln2l(res=res,ln=ln.next)
        r = [ln2l(res=[], ln=i) for i in lists]
        while None in r:
            r.pop(r.index(None))
        if len(r)==0: return
        res = reduce(lambda x,y:x+y, r) if len(r)>1 else r[0]
        res.sort()
        def newLN(m=0):
            if m<len(res):
                return ListNode(res[m], next=newLN(m=m+1))
        return newLN()