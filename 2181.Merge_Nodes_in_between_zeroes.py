# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

# Return the head of the modified linked list.

# Question Link: https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

# Intution
# There Two possible ways that i can do this question.
# I) First Way
    # 1. So the intution for this is very simple, as we are supposed take note of sum of all the node values until we reach a node with a value 0. We can consider a list containing these sums and create a linked list from this. It is as simple as it is.

    # 2. After creating the list, we have to convert that into a linked list. So as mentioned in the question "modify" the linked list, we dont have to create one and we can just go ahead modifying the present one itself.

    # 3. create a function which converts the list into a linked list. Assign first value of the list to the head node and assign dummy variable to the head node which will act as a cursor for the linked list and add the successive elements in the list to the linked list which can be done using a loop while we traverse thorugh the sum_list.

    #4. finaly after the loop ends, the current dummy node contains the last value present in the list. As we are modifying the original linked list, we need to break the linked list. And that can be done by putting "None" to dummy's next pointer.

    #5. Return the head node of the modified linked list.




# Code

# I) First Way

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def listToLL(sum_list):
            head.val = sum_list[0]
            dummy = head
            for value in sum_list[1: ]:
                dummy = dummy.next
                dummy.val = value
            
            dummy.next = None
            return head

        curr = head.next
        sum_list = []
        sum_ = 0
        while curr:
            if curr.val == 0:
                sum_list.append(sum_)
                sum_ = 0
            
            else:
                sum_ += curr.val
            
            curr = curr.next

        return listToLL(sum_list)
    

# 98.04%