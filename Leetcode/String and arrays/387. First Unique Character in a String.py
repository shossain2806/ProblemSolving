class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        seen = set()
        for index in range(l):
            if s[index] in seen:
                continue
            found = False
            for lookup_index in range(index + 1, l):
                if s[index] == s[lookup_index]:
                    found = True
                    break
            if not found:
                return index
            seen.add(s[index])
        return -1
    
    def alternateFirstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(int)
        
        for char in s:
            hashmap[char] += 1
            
        for index, char in enumerate(s):
            if hashmap[char] == 1:
                return index
        return -1
