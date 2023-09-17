from AlgorithmReusableComponents.LinkedList.linkedList import LinkedList


class RemoveDuplicateLinkedList:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def __init__(self, linkedList):
        self.linkedList = linkedList

    def removeDuplicates(self):
        currentNode = self.linkedList.head
        if currentNode is None:
            return

        nextNode = currentNode.next
        while nextNode is not None:
            if currentNode.value < nextNode.value:
                currentNode.next = nextNode
                currentNode = nextNode
            nextNode = nextNode.next
        currentNode.next = None

    def __repr__(self):
        linkedListStructure = []
        current = self.linkedList.head

        while current is not None:
            linkedListStructure.append(str(current.value))
            current = current.next

        return " -> ".join(linkedListStructure)


linkedList = LinkedList()
linkedList.constructLinkedList([1, 1, 3, 4, 4, 4, 5, 6, 6])
removedDuplicates = RemoveDuplicateLinkedList(linkedList)
removedDuplicates.removeDuplicates()
print(removedDuplicates)
