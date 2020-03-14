# 206. Reverse Linked List
#
# Reverse a singly-linked list.
#
# Implementation of iterative, recursive, and tail recursive solutions.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverse_iter(head):
    revrsd = None
    while head is not None:
        next = head.next
        head.next = revrsd
        revrsd = head
        head = next
    return revrsd

def reverse_tailrec(head, revrsd=None):
    if head is None:
        return revrsd
    next = head.next
    head.next = revrsd
    return reverse_tailrec(next, head)

def reverse_rec(head):
    """
    It's a bit unnatural to implement `reverse` in a recursive but not
    tail recursive way because it requires returning two items (thus
    requiring a helper function) and is less efficient than the tail
    recursive version, but for the purpose of an academic exercise, here
    it is.
    """
    def helper(head):
        # Empty or single-item list: reverse is list and last item is
        # item
        if head is None or head.next is None:
            return (head, head)
        # List of length >= 2: reverse rest, then attach head at end
        revrsd, last = helper(head.next)
        head.next = None
        last.next = head
        # Return the reversed list and the last node (so that additional
        # nodes can be attached)
        return (revrsd, head)
    revrsd, _ = helper(head)
    return revrsd

# Example:
#import linked
#reverse_rec(linked.List(range(5)).head)


class Solution:

    def reverseList_iter(self, head):
        return reverse_iter(head)

    def reverseList_tailrec(self, head):
        return reverse_tailrec(head)

    def reverseList_rec(self, head):
        return reverse_rec(head)

    reverseList = reverseList_iter
