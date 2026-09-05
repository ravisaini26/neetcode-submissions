class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mydict={}
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                mydict[(i,j)]=prices[j]-prices[i]
        
        max_sum=0
        max_key=0
        for k,v in mydict.items():
            if v> max_sum:
                max_sum=v
                max_key=k

        if max_sum<0:
            return 0
        else:
            return max_sum

        