# 160. Intersection of Two Linked Lists
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB
    
        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one

# 142. Linked List Cycle II
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while fast != head:
                    head = head.next
                    fast = fast.next
                return head
        
        return None

# LeetCode 19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        for i in range(n):
            fast = fast.next

        if not fast:
            head = head.next
            return head
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
