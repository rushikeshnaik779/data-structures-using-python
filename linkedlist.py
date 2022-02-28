

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None: 
            print(temp.value)
            temp = temp.next


    def append_list(self, value):
        new_node = Node(value)
        
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else : 
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1

        return True

    def pop(self):
        
        # if we don't have any item in the list 
        if self.length ==0: 
            print("Nothing to pop bro!")
            return None 
        
        # if we have 2 or more items in the list 
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp 
            temp = temp.next

        self.tail = pre 
        self.tail.next = None 
        self.length -= 1
        if self.length ==0: 
            self.head = None 
            self.tail = None 


        print(f"we poped {temp.value}")
        return temp 

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else : 
            new_node.next = self.head
            self.head = new_node
            self.length+=1

        return True

    def pop_first(self):
        
        if self.length == 0: 
            return None 
        
        temp = self.head
        self.head = self.head.next 
        temp.next = None 
        self.length -=1
        if self.length == 0: 
            self.tail = None 
        return temp 

    def get(self, index):
        if index < 0 or index >= self.length : 
            return None 

        temp = self.head 
        for _ in range(index):
            temp = temp.next

        return temp 


    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value= value 
            return True 
        return False  


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        if index == 0 :
            return self.prepend(value)
        if index == self.length: 
            return self.append_list(value)
        
        new_node = Node(value)
        temp = self.get(index - 1) 
        new_node.next = temp.next 
        temp.next = new_node

        self.length +=1
        return True


    def remove(self, index):
        
        if index < 0 or index >=self.length: 
            return None 

        if index == 0 : 
            return self.pop()

        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None   
        self.length -= 1
        return temp  

    def reverse(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp

        after = temp.next
        before = None 
        for _ in range(self.length): 
            after = temp.next 
            temp.next = before 
            before = temp 
            temp = after 







my_linked_list = Linkedlist(4)
my_linked_list.append_list(5)
my_linked_list.append_list(8)
my_linked_list.prepend(3)
my_linked_list.print_list()

print(my_linked_list.reverse())
my_linked_list.print_list()
