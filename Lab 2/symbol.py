class SymbolTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = [[]] * capacity

    def hashFunction(self, k: str):
        return (sum(map(ord, k)) % self.capacity) + 1

    def get(self, value):
        pos = self.hashFunction(value)
        if value not in self.hashtable[pos]:
            return -1
        return pos

    def insert(self, value: str):
        pos = self.get(value)
        if pos == -1:
            hashkey = self.hashFunction(value)
            self.hashtable[hashkey].append(value)
            return hashkey

        return pos



st = SymbolTable(6)
print("insert1 a", st.insert("a"))
print("insert1 b", st.insert("b"))
print("insert2 a", st.insert("a"))
print("get a", st.get("a"))
print("get c", st.get("c"))
