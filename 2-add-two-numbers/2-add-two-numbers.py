# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        start = ans
        carry = 0
        while True:
            if not l1 and not l2:
                break
            else:
                l1Num = 0
                l2Num = 0
                if l1:
                    l1Num = l1.val
                if l2:
                    l2Num = l2.val
                
                totalSum = l1Num + l2Num + carry
                
                value = totalSum % 10
                
                if totalSum > 9:
                    carry = 1
                else:
                    carry = 0
                
                
                
                ans.val = value
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
                
                if l1 or l2:
                    ans.next = ListNode()
                    ans = ans.next
        if carry == 1:
            ans.next = ListNode()
            ans.next.val = 1
        
        return start
            
        

                    
                