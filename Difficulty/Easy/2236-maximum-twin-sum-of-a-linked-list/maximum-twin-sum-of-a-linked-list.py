class Solution:
    def pairSum(self, head):
        slow = fast = head
        
        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # compute twin sums
        first = head
        second = prev
        ans = 0
        
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next
        
        return ans