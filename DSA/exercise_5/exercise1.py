class Treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def print_tree(self):
        level = ' ' * self.get_level() * 2
        print(level + self.data)
        for child in self.children:
            # print(child.data)
            child.print_tree()
            


ceo = Treenode("Nilupul(ceo)")
chinmay = Treenode("chinmay(cto)")
vishwa = Treenode("vishwa(infrastructure)")
dhaval = Treenode("dhaval(cloud mng)")
abhijit = Treenode("abhijit(app mng)")
aamir = Treenode('Aamir(application head)')
gels = Treenode("gels(hr head)")
peter = Treenode("peter(recruite)")
waqas = Treenode('waqas(policy mng)')

ceo.add_child(chinmay)
ceo.add_child(gels)
chinmay.add_child(vishwa)
chinmay.add_child(aamir)
vishwa.add_child(dhaval)
vishwa.add_child(abhijit)
gels.add_child(peter)
gels.add_child(waqas)
ceo.print_tree()





        