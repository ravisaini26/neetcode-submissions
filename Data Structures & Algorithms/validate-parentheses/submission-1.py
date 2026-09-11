class Solution:
    def isValid(self, s: str) -> bool:
        mystack=[]
        res=True
        for item in s:
            if item in ("(","{","["):
                mystack.append(item)
            elif len(mystack)==0 and item in ("]","}",")"):
                res=False
                break
            elif item in ("]","}",")"):
                if item == "]" and mystack[-1] != "[":
                    res=False
                    break
                elif item == "}" and mystack[-1] != "{":
                    res=False
                    break
                elif item == ")" and mystack[-1] != "(":
                    res=False
                    break
                else:
                    mystack.pop()
            else:
                continue
        if len(mystack)== 0:
            return res
        else:
            return False

        