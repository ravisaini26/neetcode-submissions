from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        overall_max=0
        counter={}
        while r<=len(s)-1:
            #print(f"{r=} and {s[r]=}")
            counter[s[r]]=1+counter.get(s[r],0)
            #print(f"{counter=}")
            max_freq=max(counter.values())
            if max_freq+k >= len(s[l:r+1]):      
                current_max=len(s[l:r+1])
                overall_max=max(current_max,overall_max)
                #print(f"found overall_max for {s[r]}")
            elif max_freq+k < len(s[l:r+1]):
                #print(f"removing {s[l]} from counter")
                if counter[s[l]]>1:
                    counter[s[l]]-=1
                else:
                    del counter[s[l]]
                #print(f"counter after removing {s[l]} is {counter=}")
                l=l+1
                
            r=r+1
        return overall_max
            

            






        