print(15 * "*" + 'LINK LIST' + 15 * "*")


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_ll(self):
        if self.head is None:
            print("LINK LIST IS EMPTY")
        else:
            n = self.head
            while n is not None:
                print(n.data, "----->", end=' ')
                n = n.ref

    def add_beg(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_node_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print(f"{x} not present in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_node_before(self, data, x):
        n = self.head
        if n is None:
            print("LL is empty")
            return
        if x == n.data:
            self.add_beg(data)
            return
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not empty")
            return

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    def delete_xnode(self ,x):
        if self.head is None:
            print("LL is empty")
        elif self.head.data ==x:
            self.head = self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("value not found")
            else:
                n.ref=n.ref.ref

ll1 = LinkedList()
ll1.insert_empty(1)
ll1.add_beg(10)
ll1.add_beg(20)
ll1.add_beg(30)
ll1.add_end(40)
ll1.add_node_after(35, 20)
ll1.add_node_after(5, 30)
ll1.add_node_after(15, 40)
ll1.add_node_before(4, 30)
# ll1.insert_empty(2)
ll1.add_node_before(41, 5)
# ll1.delete_begin()
# ll1.delete_begin()
# ll1.delete_begin()
ll1.delete_end()
ll1.delete_end()
ll1.delete_end()
ll1.delete_end()
ll1.delete_xnode(30)
# ll1.add_node_before(41, 12121)

ll1.traverse_ll()
