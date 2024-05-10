def CommonPrefix(s : list[str]):
    pref = s[0]
    lenght = len(pref)

    for s in s[1:]:
        while pref != s[0:lenght]:
            lenght -= 1
            if lenght == 0:
                return '""'
                
            pref = pref[0:lenght]
        
    return pref

print(CommonPrefix(["flower","flow","flight"]))
print(CommonPrefix(["dog","racecar","car"]))