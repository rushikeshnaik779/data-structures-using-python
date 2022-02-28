class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None


class Queue: 
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node 
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None: 
            print(temp.value)
            temp = temp.next

        print("*"*10, "OUTPUT ENDS HERE", "*"*10)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node 
        
        else: 
            self.last.next = new_node 
            self.last = new_node 

        self.length += 1
        return True 
    

    def dequeue(self):
        if self.length == 0 : 
            return None 
        
        temp = self.first 
        if self.length == 1: 
            self.first = None 
            self.last = None 

        else : 
            self.first = self.first.next 
            temp.next = None 
        
        self.length -= 1 
        return temp 



my_queue = Queue(0)
my_queue.print_queue()
my_queue.enqueue(10)
my_queue.enqueue(100)
my_queue.enqueue(1000)
my_queue.enqueue(10000)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()

