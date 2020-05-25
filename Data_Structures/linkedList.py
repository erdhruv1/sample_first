class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, dataList=None):
        self.head = None

        if dataList:
            node = Node(dataList.pop(0))
            self.head = node

            for data in dataList:
                node.next = Node(data)
                node = node.next

    def display(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        #nodes.append("None")

        return "->".join(nodes)

def main():

    elements = ['A', 'B', 'C', 'D', 'E']
    linkedListObj = LinkedList(elements)


    print(linkedListObj.display())

if __name__ == '__main__':
    main()