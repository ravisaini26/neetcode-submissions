from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            mysorteds="".join(sorted(s))
            if mysorteds not in res:
                res[mysorteds]=[s]
                #res[mysorteds].append(s)
            else:
                res[mysorteds].append(s)
        return list(res.values())
        
            
            
            
                
                    



