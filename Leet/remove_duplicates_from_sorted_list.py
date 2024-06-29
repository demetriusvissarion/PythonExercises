# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


def list_to_linkedlist(items):  # Helper function to convert a list to a linked list
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linkedlist_to_list(node):  # Helper function to convert a linked list to a list
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result


solution = Solution()
# Test cases
test_1 = list_to_linkedlist([1, 1, 2])
result_1 = solution.deleteDuplicates(test_1)
print("Test 1: ", linkedlist_to_list(result_1))  # should return [1, 2]

test_2 = list_to_linkedlist([1, 1, 2, 3, 3])
result_2 = solution.deleteDuplicates(test_2)
print("Test 2: ", linkedlist_to_list(result_2))  # should return [1, 2, 3]
