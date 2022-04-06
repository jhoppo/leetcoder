class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
         self.next = next
class Solution:
    """
    Runtime: 147 ms, faster than 5.10% of Python3 online submissions for Reverse Nodes in k-Group.
    Memory Usage: 19.9 MB, less than 5.60% of Python3 online submissions for Reverse Nodes in k-Group.
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        def ln2l(res: list,ln):
            if ln == None or ln == []:
                return
            else:
                res.append(ln.val)
                if ln.next == None:
                    return res
                else:
                    return ln2l(res=res,ln=ln.next)
        l = ln2l(res=[],ln=head)
        print(l)
        splitT = len(l) // k if len(l) % k == 0 else len(l)//k+1
        print(splitT)
        splitL = [l[k*n:k*(n+1):] for n in range(splitT)]
        print(f'splitL is {splitL}')
        for i in splitL:
            if len(i) == k:
                i.reverse()
        res = []
        [res.extend(splitL.pop(0)) for i in range(len(splitL))]
        print(f"res is {res}")
        def newLN(m=0):
            if m<len(res):
                return ListNode(res[m], next=newLN(m=m+1))
        return newLN()