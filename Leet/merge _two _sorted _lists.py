from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next


solution = Solution()
print("Test 1: ", solution.mergeTwoLists([1, 2, 4], [1, 3, 4]))
# test_1 should return [1,1,2,3,4,4]
print("Test 2: ", solution.mergeTwoLists([], []))
# test_2 should return []
print("Test 3: ", solution.mergeTwoLists([], [0]))
# test_3 should return [0]
