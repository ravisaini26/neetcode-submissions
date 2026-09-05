class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict={}
        myresult=[]
        for i,num in enumerate(nums):
            nums_dict[num]=i

        for i in range(len(nums)):
            if (target-nums[i]) in nums_dict and i!=nums_dict[target-nums[i]]:
                myresult.append([i,nums_dict[target-nums[i]]]) 
        return min(myresult)




        