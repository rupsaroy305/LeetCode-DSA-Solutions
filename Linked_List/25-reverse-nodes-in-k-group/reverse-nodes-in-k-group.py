class Solution:
    def reverseKGroup(self,head,k):
        cur=head
        n=0
        while cur:
            n+=1
            cur=cur.next
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while n>=k:
            cur=prev.next
            for _ in range(k-1):
                temp=cur.next
                cur.next=temp.next
                temp.next=prev.next
                prev.next=temp
            prev=cur
            n-=k
        return dummy.next