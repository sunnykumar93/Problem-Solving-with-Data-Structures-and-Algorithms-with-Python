class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head
        temp=None
        while current!=None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp


        head=prev
        l=[]
        temp=head
        return head
