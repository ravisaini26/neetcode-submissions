from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count=Counter(t)
        left=0
        right=0
        valid={}
        formed=0
        required=len(count)
        overall_min=""
        current_min=""
        while right<=len(s)-1:
            char=s[right]
            if char in count:
                if char not in valid:
                    valid[char]=1
                else:
                    valid[char]+=1

                if valid[char] == count[char]:
                    formed+=1
                    # print(f"{valid=},{right=},{left=} and {s[right]=}")

            
                
            if formed == required:
                # print(f"{valid=}")
                # print(f"{left=} and {s[left]=}")
                current_min=s[left:right+1]
                

  
                while True:
                    to_be_removed=s[left]
                    if to_be_removed not in valid:
                        left+=1
                        current_min=s[left:right+1]

                    elif to_be_removed in valid:
                        valid[to_be_removed]-=1
                        if valid[to_be_removed]<count[to_be_removed]:
                            formed-=1
                            left+=1
                            break
                        else:
                            left+=1 
                            current_min=s[left:right+1]
            # print(f"{current_min=}")
            if current_min and not overall_min:
                overall_min=current_min
            elif current_min and overall_min:
                overall_min=min([overall_min,current_min],key=len)
            else:
                pass

            right+=1
        if not overall_min:
            return ""
        else:
            return overall_min
            


