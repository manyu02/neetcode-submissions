class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range (len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            lptr,rptr=i+1,len(nums)-1
            while(lptr<rptr):
                total = nums[i] + nums[lptr] + nums[rptr]
                if total<0:
                    lptr+=1
                elif total>0:
                    rptr-=1
                else:
                    ans.append([nums[i], nums[lptr], nums[rptr]])
                    lptr += 1
                    rptr -= 1
                    while lptr < rptr and nums[lptr] == nums[lptr - 1]:
                        lptr += 1
        return ans
