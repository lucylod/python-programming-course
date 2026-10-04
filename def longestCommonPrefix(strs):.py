def longestCommonPrefix(strs):
    if not strs:
        return ""


    actual_prefix=strs[0]



    for word in strs[1:]:
        while word[:len(actual_prefix)] != actual_prefix:
            actual_prefix=actual_prefix[:-1]
            if actual_prefix == "":
                return ""
                            
    return actual_prefix

"""Eingabe"""

eingabe=input("Gib Wörter komma-separiert ein:")
strs=[x.strip() for x in eingabe.split(",")]
print(longestCommonPrefix,strs)