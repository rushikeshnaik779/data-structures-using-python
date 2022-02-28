class Node: 
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

    

# we will create empty tree at first node 
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_bst(self, value):
        new_node = Node(value)
        if self.root is None: 
            self.root = new_node
            return True 
        temp = self.root 

        while(True): 
            if new_node.value == temp.value : 
                return False 
            if new_node.value < temp.value: 
                if temp.left is None : 
                    temp.left = new_node
                    return True 
                temp = temp.left 
            else: 
                if temp.right is None : 
                    temp.right = new_node
                    return True 
                temp = temp.right 



    def contains(self, value):
        if self.root is None: 
            return False 
        temp = self.root 
        while temp is not None: 
            if value < temp.value: 
                temp = temp.left 
            elif value > temp.value: 
                temp = temp.right 
            else : 
                return True 
            
        return False 

    

my_tree = BinarySearchTree()

my_tree.insert_bst(47)
my_tree.insert_bst(21)
my_tree.insert_bst(76)
my_tree.insert_bst(18)
my_tree.insert_bst(27)
my_tree.insert_bst(52)
my_tree.insert_bst(82)
print(my_tree.contains(0))
print(my_tree.contains(82))




