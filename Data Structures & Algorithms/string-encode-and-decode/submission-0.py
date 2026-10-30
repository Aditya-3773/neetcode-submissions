class Solution:

    def encode(self, strs: List[str]) -> str:
        r= ""
        for word in strs:
            r+= str(len(word))+ "#"+ word
        return r;

    def decode(self, s: str) -> List[str]:
        r= []
        i= 0
        while i< len(s):
            j= i
            while s[j]!= "#":
                j+= 1
            length = int(s[i:j])
            word= s[j+ 1: j+ 1+ length]
            r.append(word)
            i= j+ 1+ length
        return r

