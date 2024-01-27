# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, l: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = l
        prev_node = None
        while True:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node

            if next_node is None:
                break
            cur_node = next_node

        return cur_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev_l1 = self.reverse(l1)
        rev_l2 = self.reverse(l2)

        start_node = ListNode()
        result_node = start_node

        while rev_l1 is not None and rev_l2 is not None:

            num = rev_l1.val + rev_l2.val
            rev_l1 = rev_l1.next
            rev_l2 = rev_l2.next

            result_node.val += num

            if rev_l1 is None and rev_l2 is None and result_node.val // 10 == 0:
                result_node.next = None
                break

            result_node.next = ListNode(
                    result_node.val // 10)
            result_node.val  %= 10

            result_node = result_node.next
            
        while rev_l1 is not None:

            result_node.val += rev_l1.val
            rev_l1 = rev_l1.next

            if rev_l1 is None and result_node.val // 10 == 0:
                result_node.next = None
                break
            result_node.next = ListNode(
                    result_node.val // 10)
            result_node.val  %= 10

            result_node = result_node.next
            
        while rev_l2 is not None:
            result_node.val += rev_l2.val
            rev_l2 = rev_l2.next

            if rev_l2 is None and result_node.val // 10 == 0:
                result_node.next = None
                break

            result_node.next = ListNode(
                    result_node.val // 10)
            result_node.val  %= 10
            
            
            result_node = result_node.next

        ans_node = self.reverse(start_node)
        return ans_node