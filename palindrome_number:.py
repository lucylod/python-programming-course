class Solution:
    def __init__(self, x):

        self.x=x

    def isPalindrome(self):

        x=self.x

        if x<0 or (x%10==0 and x!=0):
            return False
        
        rev_num=0

        while x>0:
            digit = x % 10
            rev_num= rev_num * 10 + digit
            x=x//10

        return rev_num == self.x 
    
    



x = int(input("Gib eine Zahl ein:"))
solver=Solution(x)
print("Ist Palindrom:", solver.isPalindrome())