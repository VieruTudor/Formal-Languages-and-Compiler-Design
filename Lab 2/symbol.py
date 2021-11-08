class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = []
        for x in range(capacity):
            self.table.append([])

    def hashFunction(self, k: str):
        return sum(map(ord, k)) % self.capacity

    def get(self, value):
        pos = self.hashFunction(value)
        if value not in self.table[pos]:
            return -1
        return pos

    def insert(self, value: str):
        pos = self.get(value)
        if pos == -1:
            hashkey = self.hashFunction(value)
            self.table[hashkey].append(value)
            return hashkey

        return pos


class SymbolTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = HashTable(capacity)

    def get(self, value):
        return self.hashtable.get(value)

    def insert(self, value: str):
        return self.hashtable.insert(value)


s = SymbolTable(6)

print(s.insert('a'))
print(s.insert('b'))
print(s.insert('a'))
print(s.get('c'))
print(s.hashtable.table)


