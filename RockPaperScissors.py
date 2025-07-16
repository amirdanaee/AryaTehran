# data
skg = {"sang","kaghaz","gheychi"}
userWin = 0
pcWin = 0
mosavi = 0
# process
bazi = input("aya bazi mikonid y|n ")
while (bazi == "y"):
    user = input("sang(s) | kaghaz(k) | gheychi(g) ")
    for x in skg:
        pc = x
        print(f"entekhab system: {pc}")
        break
    if((user == "s" and pc =="gheychi") or (user == "k" and pc == "sang") or (user == "g" and pc == "kaghaz")):
        userWin += 1
        print(f"shoma barande shodid | tedade borde shoma {userWin} | tedade borde system {pcWin} | tedade mosavi {mosavi}")
    elif((user == "s" and pc =="kaghaz") or (user == "k" and pc == "gheychi") or (user == "g" and pc == "sang")):
        pcWin += 1
        print(f"shoma bakhtid | tedade borde shoma {userWin} | tedade borde system {pcWin} | tedade mosavi {mosavi}")
    elif((user == "s" and pc =="sang") or (user == "k" and pc == "kaghaz") or (user == "g" and pc == "gheychi")):
        mosavi += 1
        print(f"mosavi shod | tedade borde shoma {userWin} | tedade borde system {pcWin} | tedade mosavi {mosavi}")
    bazi = input("aya bazi mikonid y|n ")
