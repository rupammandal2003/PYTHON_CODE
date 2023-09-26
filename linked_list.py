class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head==None:
            print("Linked list is empty.")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.next
    def add_in_the_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def add_at_the_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            else:
                n=n.next
        if n is None:
            print("Node is not present in the linked list. ")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head.data==x:
            self.add_in_the_beginning(data)
            return 
        else:
            n=self.head
            while n is not None:
                if n.next.data==x:
                    break
                else:
                    n=n.next
            if n.next is None:
                print("Node is not present in the linked list.")
                
            else:
                new_node=Node(data)
                new_node.next=n.next
                n.next=new_node
    def add_as_A_list(self,list):
        for data in list:
            self.add_at_the_end(data)
    def del_first_node(self):
        if self.head is None:
            print("linked list is empty, you can't delete node")
        else:
            self.head=self.head.next         
                    
            
ll1=linked_list()
# ll1.add_in_the_beginning(5)
# ll1.add_in_the_beginning(10)
# ll1.add_in_the_beginning(15)
# ll1.print_LL()
# ll1.add_at_the_end(17)
# ll1.add_at_the_end(19)
# ll1.print_LL()
# ll1.add_after(58,15)
# ll1.add_as_A_list(["apple","banana","mango"])
# ll1.print_LL()
# ll1.add_before("jackfruit","apple")
# ll1.add_before("lichi","mango")
# ll1.add_as_A_list([10,20,25])
# ll1.print_LL()
ll1.del_first_node()
# ll1.print_LL()