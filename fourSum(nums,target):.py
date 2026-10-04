def fourSum(nums,target):
    nums.sort()
    result=[]

    for i in range(len(nums)-3):
        if i>0 and nums[i]==nums[i-1]:
            continue

        for j in range(i+1,len(nums)-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue

            left=j+1
            right=len(nums)-1


            while left<right:
                s=nums[i]+nums[j]+nums[left]+nums[right]

                if s<target:
                    left +=1

                elif s>target:
                    right -=1

                else:
                    result.append((nums[i],nums[j],nums[left],nums[right]))
                    
                    while left<right and nums[left]==nums[left+1]:
                        left +=1


                    while left<right and nums[right]==nums[right-1]:
                        right -=1

                    left +=1
                    right -=1



    return result           

       
eingabe = input("Gib ganze Zahlen komma-separiert ein:")
liste=[int(x.strip()) for x in eingabe.split(",")]
zahl=int(input("Gib eine Zahl ein für den Target:"))
ergebnis=fourSum(liste,zahl)
print("Quadrupel mit Summe",zahl,":",ergebnis)
        


        


