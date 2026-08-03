class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def merge_list(left,right):
    a=left
    b=right
    sorted_node=Node(-1)
    temp=sorted_node

    while a is not None and b is not None:
        if a.data>b.data:
            temp.next=a
            a=a.next
            temp=temp.next
        else:
            temp.next=b
            b=b.next
            temp=temp.next
    while a is not None:
        temp.next=a
        a=a.next
        temp=temp.next
    while b is not None:
        temp.next=b
        b=b.next
        temp=temp.next
    return sorted_node.next
            
            

def find_middle_head(head):
    slow=head
    fast=head.next
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow

def sort_list(head):
    if head is None or head.next is None:
        return head
    middle=find_middle_head(head)
    left=head
    right=middle.next
    middle.next=None
    left=sort_list(left)
    right=sort_list(right)
    return merge_list(left,right)
def print_list(head):
    a=head
    while a is not None:
        print(a.data,end=' ')
        a=a.next
    

node1=Node(3)
node2=Node(2)
node3=Node(1)
node4=Node(4)
node5=Node(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5


head=node1

head1=sort_list(head)
print_list(head1)




            

