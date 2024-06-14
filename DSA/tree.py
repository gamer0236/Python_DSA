class Treenode:
    def __init__(self,data):
        self.data =data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()
            # print(child.data)

def build_product():
    electronic = Treenode("Electronics")
    laptop = Treenode("laptop")
    phone = Treenode("phone")
    electronic.add_child(laptop)
    electronic.add_child(phone)
    # phone.add_child(Treenode("vivo"))
    electronic.print_tree()

build_product()