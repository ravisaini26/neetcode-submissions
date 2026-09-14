class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        first_index=l
        last_index=r
        near_end=False
        near_front=False

        try:

            while l<r:
                if nums[l+1]>=nums[l] and nums[r]>=nums[r-1]:
                    l=l+1
                    r=r-1
                elif nums[l+1]<nums[l]:
                    last_index=l
                    first_index=l+1
                    near_front=True
                    break
                elif nums[r-1]>nums[r]:
                    last_index=r-1
                    first_index=r
                    near_end=True
                    break
            
            if first_index==0 and last_index == len(nums)-1:
                return nums[0]
            else:
                if near_end:
                    i=first_index
                    while len(nums)-i !=0:
                        item=nums.pop()
                        nums.insert(0,item)
                        i+=1
                    return nums[0]
                elif near_front:
                    j=last_index
                    while j>=0:
                        item=nums.pop(0)
                        nums.append(item)
                        j-=1
                    return nums[0]
        except Exception as e:
            print(e)


        

            

                
