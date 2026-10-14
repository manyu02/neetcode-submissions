class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        nums={0,1,2,3,4,5,6,7,8,9}
        i=0
        while i< len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            res.append(s[i:i+length])
            i+=length
        return res
                    
                        