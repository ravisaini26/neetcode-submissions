class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_checker={}
        max_streak=0
        current_streak=0
        left=0
        i=0
        while i!=len(s):
            if s[i] not in unique_checker:
                unique_checker[s[i]]=i
                current_streak=len(s[left:i+1])
                
               # print(f"{i=} and {s[i]=}")
            elif s[i] in unique_checker and unique_checker[s[i]]<left:
                unique_checker[s[i]]=i
                current_streak=len(s[left:i+1])
               
            elif s[i] in unique_checker and unique_checker[s[i]]>=left:
                
                current_streak=len(s[left:i])
                # print(f"{s[left:i]=}")
                left=unique_checker[s[i]]+1
                unique_checker[s[i]]=i
           
            if current_streak>max_streak:
                max_streak=current_streak
            i+=1  
        return max_streak


        