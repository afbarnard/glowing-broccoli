# 234. Palindrome Linked List
#
# Given a singly linked list, determine if its items form a palindrome.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def is_palindrome_rec(head):
    def build_stack(node, revrsd, length):
        if node is None:
            return revrsd, length
        return build_stack(node.next, (node.val, revrsd), length + 1)
    def equal_n(node, pair, length):
        if length == 0:
            return True
        val1 = node.val
        val2, tail = pair
        if val1 != val2:
            return False
        return equal_n(node.next, tail, length - 1)
    stack, stack_size = build_stack(head, (), 0)
    return equal_n(head, stack, stack_size // 2)

def is_palindrome_iter(head):
    # Build a stack of the items
    stack = []
    node = head
    while not node is None:
        stack.append(node.val)
        node = node.next
    # Compare the stack to the list
    node = head
    for idx in range(len(stack) // 2):
        val1 = node.val
        val2 = stack[-1]
        if val1 != val2:
            return False
        node = node.next
        del stack[-1]
    return True

class Solution:

    def isPalindrome_rec(self, head: ListNode) -> bool:
        return is_palindrome_rec(head)

    def isPalindrome_iter(self, head: ListNode) -> bool:
        return is_palindrome_iter(head)

    isPalindrome = isPalindrome_iter
