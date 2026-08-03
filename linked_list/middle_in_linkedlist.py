class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def create_single_ll_from_array(arr):
    head = Node(arr[0])
    a = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        a.next = new_node
        a = a.next
    return head
def print_single_ll(head):
    a = head
    print(a.data, end=" ")
    while a.next is not None:
        a = a.next
        print(a.data, end=" ")
    print()

def middle_of_single_ll(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

head= create_single_ll_from_array([10, 20, 30, 40])
print(middle_of_single_ll(head).data)  # Output: 30 here use the head.data to get the value of the middle node, or u will get that space complexity some shit
