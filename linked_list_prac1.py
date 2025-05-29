class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class singleLinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Linked list is empty")

L=singleLinkedlist()
n=Node(10)
L.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
L.display()



class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SLL:
    def create_ll(self,n_terms):
        i=1
        self.head=Node(i**2)
        temp=self.head
        while i < n_terms:
            i+=1
            temp2=Node(i**2)
            temp.next=temp2
            temp=temp2

            print("Linked list created")
            return self.head
    def print_ll(self,n_terms):
        temp=self.create_ll(n_terms)
        print("printing linked list")
        while temp.next:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data)

obj=SLL()
obj.print_ll(10)

            


# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class sll:
#     def create_link_list(self,n_terms):
#         i=1
#         self.head=Node(i**2)
#         temp=self.head
#         while i< n_terms:
#             i+=1
#             temp2=Node(i**2)
#             temp.next=temp2
#             temp=temp2
#         print("linked list created")
#         return self.head
    
#     def print_ll(self,n_terms):
#         temp= self.create_link_list(n_terms)
#         print("printing linked list")
#         while temp.next:
#             print(temp.data,end=" ")
#             temp=temp.next
#         print(temp.data)


# obj=sll()
# obj.print_ll(10)