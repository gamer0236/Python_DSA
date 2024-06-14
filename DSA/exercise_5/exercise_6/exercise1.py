class Binarytreenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,child):
        if child == self.data:
            return

        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = Binarytreenode(child)

        if child > self.data:
            if self.right:
                self.right.add_child(child)
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
    
    def post_order(self):
        element = []

        if self.left:
            element += self.left.post_order()

        if self.right:
            element += self.right.post_order()

        element.append(self.data)

        return element

    def pre_order(self):
        element = []

        element.append(self.data)

        if self.left:
            element += self.left.pre_order()

        if self.right:
            element += self.right.pre_order()

        return element


    
    def serach(self,val):
        if val == self.data:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.serach(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.serach(val)
            else:
                return False


    
    def find_min(self):
        treelist = self.inorder_traversal()
        return treelist[0]
    
    def find_max(self):
        treelist = self.inorder_traversal()
        return treelist[-1]
    
    def calculate_sum(self):
        treelist = self.inorder_traversal()
        sum = 0
        for i in treelist:
            sum += i
        return sum
        



def build_tree(elemnts):
    root = Binarytreenode(elemnts[0])

    for i in range(1,len(elemnts)):
        root.add_child(elemnts[i])

    return root


numbers = [45,34,7,76,5,335,31,768,243,2123,1,2,3]
tree = build_tree(numbers)
print(tree.inorder_traversal())
print(tree.post_order())
print(tree.pre_order())
print(tree.find_min())
print(tree.find_max())
print(tree.calculate_sum())
print(tree.serach(5))