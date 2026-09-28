class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif not nums:
            return 0
        else:
            left=0
            right=1
            sequence=1
            max_seq=0
            nums_set=set(nums)
            nums.sort()
            while right<=len(nums)-1:
                

                if nums[right]== nums[right-1]:
                    max_seq=max(sequence,max_seq)
                    right=right+1
                elif nums[right] == nums[left]+sequence:
            
                    sequence+=1
                    
                    right=right+1
                    max_seq=max(sequence,max_seq)
                else:
                    max_seq=max(sequence,max_seq)
                    left=right
                    right+=1
                    sequence=1
                
            return max_seq

        


        