class Binarytreenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,child):
        if self.data == child:
            return Binarytreenode(child)
        
        if child < self.data:
            if self.left:
                return self.left.add_child(child)
            else:
                self.left = Binarytreenode(child)

        if child > self.data:
            if self.right:
                return self.right.add_child(child)
            else:
                self.right = Binarytreenode(child)


    def inorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        

    def delete_item(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_item(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_item(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_item(min_val)

        return self





    
def build_tree(element):

    root = Binarytreenode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])

    return root

numbers = [17,4,1,20,9,23,180,34]
tree = build_tree(numbers)
print(tree.inorder_traversal())
print(tree.find_max())
tree.delete_item(20)
print(tree.inorder_traversal())





        