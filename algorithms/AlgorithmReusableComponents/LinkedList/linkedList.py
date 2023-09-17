class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def constructLinkedList(self, arrayList):
        for i in arrayList:
            self.insert(i)

    def insert(self, value):
        newNode = LinkedListNode(value)
        current = self.head

        if current is None:
            self.head = newNode
            return

        while current.next:
            current = current.next
        current.next = newNode
