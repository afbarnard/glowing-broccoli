# 141. Linked List Cycle
#
# Given a singly-linked list, determine if it has a cycle.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def has_cycle_set(head):
    seen = set()
    node = head
    while node is not None:
        if node in seen:
            return True
        seen.add(node)
        node = node.next

def has_cycle_two_ptrs1(head):
    node1 = head
    node2 = head
    idx = 0
    while node2 is not None:
        # If the two nodes are the same (and it's not the beginning),
        # there is a cycle
        if idx % 2 == 0 and idx > 0 and node1 == node2:
            return True
        # Otherwise, continue
        node2 = node2.next
        if idx % 2 == 0:
            node1 = node1.next
        idx += 1
    return False

def has_cycle_two_ptrs2(head):
    node1 = head
    node2 = head
    incremented = False
    while node2 is not None:
        # If the two nodes are the same (and it's not the beginning),
        # there is a cycle
        if incremented and node1 == node2:
            return True
        # Otherwise, continue
        node1 = node1.next
        node2 = node2.next
        if node2 is not None:
            node2 = node2.next
        incremented = True
    return False


class Solution:

    def hasCycle1(self, head: ListNode) -> bool:
        return has_cycle_set(head)

    def hasCycle2(self, head: ListNode) -> bool:
        return has_cycle_two_ptrs1(head)

    def hasCycle3(self, head: ListNode) -> bool:
        return has_cycle_two_ptrs2(head)

    hasCycle = hasCycle1
