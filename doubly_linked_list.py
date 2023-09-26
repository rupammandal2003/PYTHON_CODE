class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly_linkeed_list:
    def __init__(self):
        self.head=None
    def print_ll_forward(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(f"{n.data} <-->",end=" ")
                n=n.next
    def print_ll_backward(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            while n is not None:
                print(f"{n.data} <-->",end=" ")
                n=n.prev
    def add_begin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
            new_node.prev=n
    def add_after(self,data,x):
        
        if self.head is None:
            print("doubly linked list is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                    # new_node.next=n.next
                    # n.next.prev=new_node
                    # new_node.prev=n
                    # n.next=new_node
                else:
                    n=n.next
            if n is None:
                print("node is not found in the linked list")
            else:
                new_node=node(data)
                new_node.next=n.next
                new_node.prev=n
                if n.next is not None:
                    n.next.prev=new_node
                n.next=new_node
    def add_before(self,data,x):
        new_node=node(data)
        if self.head is None:
           print("Doubly linked list is empty")
           
        elif self.head.data==x:
            self.add_begin(data)
            
        else:
            n=self.head
            while n is not None:
                if n.next.data==x:
                    break
                    # new_node.next=n.next
                    # n.next.prev=new_node
                    # new_node.prev=n
                    # n.next=new_node
            if n is None:
                print("node is not found in the linked list")
            else:
                new_node.next=n.next
                n.next.prev=new_node
                new_node.prev=n
                n.next=new_node
                    

                
dl1=doubly_linkeed_list()
dl1.add_begin(5)
dl1.add_end(10)
dl1.add_end(15)
# dl1.add_after(20,10)
# dl1.add_before(10,25)
# dl1.add_begin(10)
# dl1.add_begin(15)
dl1.print_ll_forward()
# dl1.print_ll_backward()             