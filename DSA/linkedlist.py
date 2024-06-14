class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_in_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)


def main():
    ll = Linkedlist()
    ll.insert_in_begining(5)
    ll.insert_in_begining(89)
    ll.print()
    
        
main()      