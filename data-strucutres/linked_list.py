# Python program to create linked list and its main functionality
# push, pop and print the linked list

# Node class 
class Node: 
    # Constructor to initialize 
    # the node object 
    def __init__(self, data): 
      self.data = data 
      self.next = None

# LinkedList class
class LinkedList: 
    # Function to initialize head 
    def __init__(self): 
      self.head = None

    # Function to insert a new node at the beginning 
    def push(self, new_data): 
      new_node = Node(new_data) 
      new_node.next = self.head 
      self.head = new_node 


    # Remove an item from the LinkedList
    def pop(self, key):
      temp = self.head

      # If head node itself holds the key to be deleted
      if(self.head.data == key):
        self.head = temp.next
        temp = None
        return

      # this loop is to just set the prev node
      while (temp is not None):
        if(temp.data == key):
          break
        else:
          prev = temp
          temp = temp.next

      #after the loop just change the next node   
      if(temp == None):
        return
      prev.next = temp.next
      temp = None

    # Utility function to print it the linked LinkedList 
    def printList(self): 
      temp = self.head 
      while(temp): 
        print(temp.data) 
        temp = temp.next

# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
llist.printList()
llist.pop(4)
llist.printList()