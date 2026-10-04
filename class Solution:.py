class Solution:
    def lengthOfLongestSubstring(self,s):
        sub={}
        cur_sub_start = 0
        cur_len=0
        longest=0

        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= cur_sub_start:
                cur_sub_start = sub[letter]+1
                cur_len=i-sub[letter]
                sub[letter]=i

            else:
                sub[letter]=i
                cur_len+=1
                if cur_len>longest:
                    longest = cur_len

        return longest



s = input("Gib einen neuen String ein:")
solver=Solution()
result=solver.lengthOfLongestSubstring(s)

print("Länge des längsten Substrings ohne Wiederholung:", result)



