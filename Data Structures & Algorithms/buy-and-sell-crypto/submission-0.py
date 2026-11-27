class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=prices[0]
        profit=0
        for i in range(len(prices)):
            l=min(prices[i],l)
            if profit<prices[i]-l:
                profit=prices[i]-l
        return profit
        
            
            


        