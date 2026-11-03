class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen= set()
        i= 0
        j= 0
        c= 0
        while j< len(s):
            if s[j] not in seen:
                seen.add(s[j])
                c= max(c, j- i+ 1)
                j+= 1

            else:
                seen.remove(s[i])
                i+= 1

        return c