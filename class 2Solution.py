class Solution:
    def __init__(self, s, p):
        self.s=s
        self.p=p
        self.memo={}

    def isMatch(self):
        return self._match(0,0)
        
       

    def _match(self, i, j):
     
        if (i,j) in self.memo:
            return self.memo[(i,j)]
        
        s=self.s
        p=self.p


        if j == len(p):
            return i == len(s)
    
        first_match= (i<len(s)) and (p[j] == s[i] or p[j] == ".")

        if j+1 < len(p) and p[j+1]=="*":
            ans = self._match(i,j+2) or (first_match and self._match(i+1,j))
        
        else: 
            ans = first_match and self._match(i+1, j+1)



        self.memo[(i,j)] = ans

        return ans