class Solution:
    def removeNthFromEnd(self,head,n):
        a=[]
        p=head
        while p:
            a.append(p)
            p=p.next
        i=len(a)-n
        if i==0:return head.next
        a[i-1].next=a[i].next
        return head