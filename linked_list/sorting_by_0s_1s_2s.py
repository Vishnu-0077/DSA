class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def sort_list(head):
    temp=head
    a=head
    count_0=0
    count_1=0
    count_2=0
    while a is not None:
        if a.data==0:
            count_0+=1
        elif a.data==1:
            count_1+=1
        else:
            count_2+=1
        a=a.next
    a=temp
    while a is not None:
        if count_0!=0:
            a.data=0
            count_0-=1
        elif count_1!=0 and count_0==0:
            a.data=1
            count_1-=1
        elif count_2!=0 and count_0==0 and count_1==0:
            a.data=2
            count_2-=1
        a=a.next
    return temp #i have a doubt here so we can just use make a new ll and return new_list.next, where before the loop we set this new_list as head with value -1

def print_list(head):
    a=head
    while a is not None:
        print(a.data,end=' ')
        a=a.next

node1=Node(1)
node2=Node(1)
node3=Node(2)
node4=Node(0)
node5=Node(1)
node6=Node(2)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6

head=node1
print_list(head)
print()
head=sort_list(head)
print_list(head)

# other method is just make 3 different dummy list and add 0's, 1's and 2's in their respective places and then join them