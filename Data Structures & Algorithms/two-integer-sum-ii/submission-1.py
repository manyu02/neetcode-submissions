class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        lptr,rptr=0,len(numbers)-1
        while(lptr<rptr):
            if (numbers[lptr]+numbers[rptr])==target:
                return[lptr+1,rptr+1]
                
            elif (numbers[lptr]+numbers[rptr])<target:
                lptr+=1
            else:
                rptr-=1
       

        