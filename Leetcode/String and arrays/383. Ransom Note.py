class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        hashmap_magazine = defaultdict(int)
        
        for char in magazine:
            hashmap_magazine[char] += 1
            
        for char in ransomNote:
            hashmap_magazine[char] -= 1
            if hashmap_magazine[char] < 0:
                return False
            
        return True