class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # creating doubly linked list
    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL has been created successfully"
    
    # inserting element in a doubly linked list
    def insertDLL(self,nodeValue,location):
        if self.head is None :
            print("The node cannot be  inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0 :
                newNode.prev = None 
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1 :
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1 
                newNode.next = tempNode.next 
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    # traversing in a linked list
    def traverseDLL(self):
        if self.head is None :
            print ("List is Empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next 
                
                
    # reverse traversal in doubly linked list
    def reverseTraversalDLL(self):
        if self.head is None:
            print("List is Empty")
        else:
            tempNode = self.tail
            while tempNode :
                print(tempNode.value)
                tempNode = tempNode.prev
                
    # searching in alindef list
    def searchDLL(self,nodeValue):
        if self.head is None :
            print("List is Empty")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue :
                    return tempNode.value
                tempNode = tempNode.next
            return "Node not Found"
            
    # deletion is a dobuly linked list
    def deleteNode(self,location):
        if self.head is None :
            print("List is empty")
        else :
            if location == 0:
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1 :
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location - 1 :
                    curNode = curNode.next  
                    index +=1 
                curNode.next = curNode.next.next 
                curNode.next.prev = curNode
            print("The list has been Deleted!")
                
                
    # deleting the entire list
    def deleteDLL(self):
        if self.head is None:
            print("List is Empty")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The Entire List has been deleted")
    
    
    
    
    
    
# for testing/ printing our doubly linked list
doublyLL = DoublyLinkedList()
doublyLL.createDLL(5) 

doublyLL.insertDLL(0,0) 
doublyLL.insertDLL(2,1) 
doublyLL.insertDLL(7,2) 
print([node.value for node in doublyLL])
# doublyLL.traverseDLL() 
# doublyLL.reverseTraversalDLL() 
# print(doublyLL.searchDLL(6) )
# doublyLL.deleteNode(-1) 
# we need to insert - sign to delete node at respective  places
doublyLL.deleteDLL() 

print([node.value for node in doublyLL])
