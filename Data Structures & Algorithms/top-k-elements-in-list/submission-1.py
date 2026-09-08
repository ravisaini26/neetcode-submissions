class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mynumsdict={}
        for i in nums:
            if i in mynumsdict:
                mynumsdict[i]+=1
            else:
                mynumsdict[i]=1
        mycouplelist=[]
        for x,y in mynumsdict.items():
            mycouplelist.append([x,y])
        mycouplelist.sort(key=lambda z:z[1],reverse=True)
        
        final=[]
        for i in range(k):
            key,val=mycouplelist[i]
            
            final.append(key)
        return final

        