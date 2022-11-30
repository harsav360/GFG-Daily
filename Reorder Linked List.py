Given a singly linked list: A0→A1→...→An-2→An-1, reorder it to: A0→An-1→A1→An-2→A2→An-3→...
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: It is recommended do this in-place without altering the node's values.
  
  
  Space Complexity -> O(1) and Time Complexity -> O(N)

  
def reorderList(self,head):
        #First find out the middle of the linked List
        slow,fast = head,head.next #Use slow and fast pointer approach
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Split the linked list into two parts
        #1->2->3->4->->5->6->7->8->9->X
        #First Part = 1->2->3->4->->5->X
        #Second Part = 6->7->8->9->X
        second = slow.next
        slow.next = None 
        
        #Now Reverse the second linked list
        curr = second
        prev,ahead = None,None
        
        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        second = prev
        first = head
        while second:
            ptr1,ptr2 = first.next,second.next
            first.next = second
            second.next = ptr1
            first,second = ptr1,ptr2
