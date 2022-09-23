class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap = defaultdict(int)
        
        for char in s:
            hashmap[char] += 1
            
        for char in t:
            hashmap[char] -= 1
        
        for key in hashmap:
            if hashmap[key] != 0:
                return False
        return True