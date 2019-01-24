def match(node1, node2):
    return node1.a == node2.a or node1.b == node2.b or node1.a == node2.b or node1.b == node2.a


class Node(object):
    def __init__(self, next_node, a, b):
        self.next = next_node
        self.a = a
        self.b = b


class LinkedList(object):
    def __init__(self):
        self.nodes = []
        self.first = None
        self.last = None

    def addNode(self, a, b):
        self.nodes.append(Node(None, a, b))

    def orderNodes(self):
        self.first = self.nodes[0]
        self.last = self.nodes[0]
        t = self.nodes
        while t:
            for node in t:
                if match(self.first, node):
                    node.next = self.first
                    self.first = node
                    t.remove(node)
                elif match(self.last, node):
                    self.last.next = node
                    self.last = node
                    t.remove(node)

    def getSize(self):
        return len(self.nodes)

    def getSorted(self):
        self.orderNodes()
        sort = []
        t = self.first
        while(t.next != t):
            if (t.a == t.next.a or t.a == t.next.b) and (t.b != t.next.a and t.b != t.next.b):
                sort.append(t.a)
            else:
                sort.append(t.b)
            t = t.next

        return list(reversed(sort))

LL = LinkedList()
LL.addNode('A','0') # <--start!
LL.addNode('E','D')
LL.addNode('E','F')
LL.addNode('B','A')
LL.addNode('D','C')
LL.addNode('B','C')
LL.addNode('F','1') # <--end!

print(LL.getSorted())