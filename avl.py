from node import Node

def comp_1(node_1, node_2):
    return node_1 < node_2
    pass

class AVLTree:
    def __init__(self, compare_function = comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function
    def get_height(self, node):
        if node:
            return node.height
        else:
            return 0
        
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left) , self.get_height(node.right))

    def get_balance(self,node):
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x
    
    def insert(self,value):
        self.root = self._insert(self.root , value)
    
    def _insert(self, node , value):
        if not node:
            new_node = Node()
            new_node.value = value
            self.size += 1
            return new_node
        
        if self.comparator(value, node.value):
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right , value)

        self.update_height(node)
        balance = self.get_balance(node)



#to be continued..............












    def remove(self, value):
        self.root = self._remove(self.root , value)

    def _remove(self, node, value):
        if not node:
            return node
        
        if self.comparator(value, node.value):
            node.left = self._remove(node.left, value)
        elif self.comparator(node.value, value):
            node.right = self._remove(node.right, value)
        else:
            self.size -= 1
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            







    def get_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self.root = inorder(self.root, result)
        return result


    def inorder(self, node , result):
        if not node:
            return 
        self.inorder(node.left, result)
        result.append(node.value)
        self.inorder(node.right, result)
        


    


        

