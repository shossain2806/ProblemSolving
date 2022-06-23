class DisJointSet:
    
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def union(self, x, y):
        self.root[y] = x
    
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    
    
df = DisJointSet(10)
df.union(1, 2)
df.union(2, 5)
df.union(5, 6)
df.union(6, 7)
df.union(3, 8)
df.union(8, 9)
print(df.connected(1, 5))  # true
print(df.connected(5, 7))  # true
print(df.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
df.union(9, 4)
print(df.connected(4, 9))  # true