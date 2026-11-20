class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         ss = sorted(s.lower())
         tt = sorted(t.lower())
         if ss == tt:
           return True

         if ss != tt: 
           return False