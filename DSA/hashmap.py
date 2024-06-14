class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]





t = HashTable()
print(t.get_hash("march 6"))
t.add('march 6',130)
t.add('march 5',120)
print(t.arr)
print(t.get("march 6"))
print(t.get('march 5'))


hs = ord("a")
print(hs)
