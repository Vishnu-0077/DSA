class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        

def create_double_ll_from_array(arr):
    head=Node(arr[0])
    a=head
    for i in range(1,len(arr)):
        new_node=Node(arr[i])
        a.next=new_node
        new_node.prev=a
        a=a.next
    return head

def reverse_dll(head):
    a=head
    while a.next is not None:
        a=a.next
    head=a
    while a is not None:
        temp_n=a.next
        temp_p=a.prev
        a.next=a.prev
        a.prev=temp_n
        a=temp_p    
    return head

def print_dll(head):
    a=head
    print(a.data, end=" ")
    while a.next is not None:
        a=a.next
        print(a.data, end=" ")
    print()

print('brefore reversing:')
head = create_double_ll_from_array([10, 20, 30, 40, 50])
print_dll(head)
print('after reversing:')
head = reverse_dll(head)
print_dll(head)



    