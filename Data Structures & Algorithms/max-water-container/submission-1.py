class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr,rptr=0,len(heights)-1
        ans=0
        while(lptr<rptr):
            area= (rptr-lptr)*min(heights[lptr],heights[rptr])
            if heights[lptr]<heights[rptr]:
                lptr+=1
            else:
                rptr-=1
            ans=max(ans,area)
        return ans

