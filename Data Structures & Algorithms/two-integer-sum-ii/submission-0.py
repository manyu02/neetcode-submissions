class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        # while (l<r):
        #     mid=(l+r)//2
        #     if (numbers[mid]==target):
        #         break
        #     if numbers[mid]<target:
        #         l=mid
        #     else:
        #         r=mid
        lptr,rptr=0,len(numbers)-1
        for i in range(len(numbers)):
            if (numbers[lptr]+numbers[rptr])==target:
                ans.append(lptr+1)
                ans.append(rptr+1)
                break
            elif (numbers[lptr]+numbers[rptr])<target:
                lptr+=1
            else:
                rptr-=1
        return ans

        