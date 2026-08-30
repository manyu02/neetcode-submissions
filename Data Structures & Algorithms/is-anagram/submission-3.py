class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters={}
        val=0
        if len(s)!=len(t):
            return False
        for i in s:
            if i in letters:
                letters[i]+=1
            else:
                letters[i]=1
        for i in t:
            if i in letters:
                letters[i]-=1
                if letters[i]==0:
                    letters.pop(i)
            else:
                return False
        return True

