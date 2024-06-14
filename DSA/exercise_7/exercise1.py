class Binarytreenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.rigth = None
    
    def add_child(self,child):
        
        if child == self.data:
            return Binarytreenode(child)
        
        if child < self.data:
            if self.left:
                return self.left.add_child(child) 
            else:
                self.left = Binarytreenode(child)

            

        if child > self.data:
            if self.rigth:
                return self.rigth.add_child(child)
            else:
                self.rigth = Binarytreenode(child)


    def find_max(self):
        if self.rigth:
            return self.rigth.find_max()
        else:
            return self.data

    def inorder_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.rigth:
            elements += self.rigth.inorder_traversal()
        
        return elements
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.rigth:
                self.rigth = self.rigth.delete(val)
        else:
            if self.left is None and self.rigth is None:
                return None
            elif self.left is  None:
                return self.rigth
            elif self.rigth is None:
                return self.left
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)


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
tree.delete(20)
print(tree.inorder_traversal())

            
