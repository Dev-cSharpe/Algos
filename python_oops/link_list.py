class LinkList():
    def __init__(self,val):
        self.val=val
        self.nextPtr=None
    
    def add_node(self,val):
        self.nextPtr=LinkList(val)
        return self.nextPtr        

a=LinkList(1)
head=a
for i in range(2,6):
    a=a.add_node(i)


while head is not None:
    print(head.val)
    head=head.nextPtr
