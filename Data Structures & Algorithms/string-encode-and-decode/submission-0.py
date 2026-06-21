class Solution:

    def encode(self, strs: List[str]) -> str:
        k=''
        for i in strs:
            k+=str(len(i))+'#'+i
        return k
    def decode(self, s: str) -> List[str]:
        l=[]
        n=''
        j = 0
        while j < len(s): 
            if s[j].isnumeric():
                n+=s[j]
                j+=1
            else:
                l.append(s[j+1:j+int(n)+1])
                j+=int(n)+1
                n=''
        return l
        


