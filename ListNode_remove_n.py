# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = [head]
        proList = []
        while len(tmp) > 0:
            tmpPop = tmp.pop()
            proList.append(tmpPop.val)
            if tmpPop.next != None:
                tmp.append(tmpPop.next)
        proList.pop(-n)
        def newLN(m=0):
            if m<len(proList):
                return ListNode(proList[m], next=newLN(m=m+1))
        return newLN()