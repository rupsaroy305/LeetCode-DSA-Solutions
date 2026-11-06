class Solution:
    def mergeKLists(self, lists):
        values = []
        for head in lists:
            current = head
            while current:
                values.append(current.val)
                current = current.next
        values.sort()
        dummy = ListNode(0)
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next