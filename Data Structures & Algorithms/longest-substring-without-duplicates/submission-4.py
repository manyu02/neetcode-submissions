class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        seen=set()
        ans=0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                ans=max(ans,r-l+1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                ans = max(ans, r - l + 1)
        return ans

