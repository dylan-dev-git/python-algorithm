class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self,data):
    newNode = Node(data)
    self.head = newNode
    self.tail = newNode
    self.count = 1

  def append(self,data):
    newNode = Node(data)
    self.tail.next = newNode
    self.tail = newNode
    self.count += 1
  
  def printList(self):
    print("total : " + str(self.count))
    nodeData = self.head
    while(True):
      print(nodeData.data)
      if nodeData.next == None:
        break
      nodeData = nodeData.next

  

listData = LinkedList(1)
listData.append(2)
listData.append(3)
listData.printList()

    





