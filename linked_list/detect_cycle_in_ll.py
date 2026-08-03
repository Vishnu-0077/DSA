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
def detect_cycle(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            return True
    return False
head = create_single_ll_from_array([10, 20, 30, 40])
print(detect_cycle(head))  # Output: False

#alse check the brute force method where we store the values in a set and check if the value is already present in the set, if yes then return true else return false