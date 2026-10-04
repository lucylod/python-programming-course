def threeSumClosest(nums, target):
    nums.sort()

    best_sum=nums[0]+nums[1]+nums[2]

    for i in range(len(nums)-2):
        left=i+1
        right=len(nums)-1
        while left < right:
            s=nums[i]+ nums[left] + nums[right]
            if abs(s-target)<abs(best_sum-target):            
                best_sum=s

            if s<target:
                left+=1

            elif s>target:

                right -=1

            else:

                return s
            
    return best_sum

"""Eingabe"""

eingabe = input(
    "Gib ganze Zahlen komma-separiert ein:"
)
nums=[int(x.strip()) for x in eingabe.split(",")]
target=int(input("Gib eine Zahl ein:"))
ergebnis= threeSumClosest(nums,target)
print("Nächste Summe", ergebnis)




        
    

        
