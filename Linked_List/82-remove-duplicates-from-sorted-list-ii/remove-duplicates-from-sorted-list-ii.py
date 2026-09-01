class Solution:
    def deleteDuplicates(self,head):
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next:
            q=p.next
            while q.next and q.val==q.next.val:
                q=q.next
            if p.next!=q:
                p.next=q.next
            else:
                p=p.next
        return dummy.next