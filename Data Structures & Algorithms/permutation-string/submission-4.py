class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        size = len(s1)
        s1 = ''.join(sorted(s1))

        i = 0
        while i < len(s2):
            window = s2[i:i+size]
            if (s1 == ''.join(sorted(window))):
                return True
            i = i+1
        
        return False