class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        seen=dict()
        for i in range(len(nums)):
            x=target-nums[i]
            if nums[i] in seen:
                answer.append(seen[nums[i]])
                answer.append(i)
                return answer
            else:
                seen[x]=i
