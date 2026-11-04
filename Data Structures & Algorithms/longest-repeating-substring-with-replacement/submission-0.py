class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen= {}
        r= 0
        i= 0
        m= 0
        
        for j in range(len(s)):
            seen[s[j]]= seen.get(s[j], 0)+ 1
            m= max(m, seen[s[j]])

            while (j- i+ 1)- m> k:
                seen[s[i]]-= 1
                i+= 1

            r= max(r, j- i+ 1)
        return r