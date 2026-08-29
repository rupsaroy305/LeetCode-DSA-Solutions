class Solution:
    def rotateRight(self,head,k):
        if not head or not head.next:return head
        a=[]
        p=head
        while p:
            a.append(p)
            p=p.next
        k%=len(a)
        if k==0:return head
        a[-k-1].next=None
        a[-1].next=head
        return a[-k]