class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def pre_order(root):
    if root:
        print root.info,
        if root.left and root.right:
            pre_order(root.left)
            pre_order(root.right)
        elif root.left:
            pre_order(root.left)
        elif root.right:
            pre_order(root.right)

tree = BinarySearchTree()
#arr = [1, 2, 5, 3, 4, 6]
arr = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
for i in xrange(len(arr)):
    tree.create(arr[i])

pre_order(tree.root)