class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_till_now=1
        mul_till_array=[]
        res=[]
        for index,item in enumerate(nums):
            mul_till_now=mul_till_now*item
            mul_till_array.append(mul_till_now)
           # print(f"{mul_till_array=}")
            back_all_mul=1
        for i in range(len(mul_till_array)-1,-1,-1):
           # print(f"{i=}")
            if i == 0:
                res.append(back_all_mul)
            else:
                res.append(mul_till_array[i-1]*back_all_mul)
            #print(f"{res=} and {back_all_mul} and {mul_till_array[i-1]}")
            back_all_mul=back_all_mul*nums[i]
        return list(reversed(res))

       

            
        

        