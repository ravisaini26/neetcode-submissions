class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_s="".join(filter(str.isalnum,s)).lower()
        print(f"{updated_s=}")
        if updated_s==updated_s[::-1]:
            return True
        else:
            return False
        