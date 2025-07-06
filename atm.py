# data
passWord = "1234"
accountBalance = 1000000
# process
passWordEntered =  input("lotfan ramze karte khod ra vared namayid: ")
if (passWordEntered == passWord):
    print("shoma ba movafaghiyat vared shodid")
    print("lotfan amliyat khod ra entekhab konid: ")
    requestType = int (input("1-bardasht mojodi  2-enteghal vajeh 3-taghir ramze kart: "))
    if(requestType == 1):
       requestAccountBalance = int(input("lotfan mablagh bardasht khod ra vared namayid: "))
       if(requestAccountBalance <= accountBalance):
        #    accountBalance = accountBalance - requestAccountBalance
           accountBalance -= requestAccountBalance
           print("lotfan vajeh khod ra bardeshat konid")
        #    print("mande mojodi shoma:" + requestAccountBalance)
           print("mande mojodi shoma")
           print(accountBalance)
           print("lotfan karte khod ra bardarid.")
       else:
           print("mojodi shoma baraye bardasht kafi nemibashd.")
    elif(requestType == 2):
        destinationCardNumber = input("lotfan shomre kart maghsad ra vared namayid: ")
        transferAmount = int (input("lotfan mablagh morde enteghal ra vared namayid:"))
        if(transferAmount <= accountBalance):
            accountBalance = accountBalance - transferAmount
            print("enteghale vajh anjam shod.")
            print("lotfan karte khod ra bardarid.")
        else:
             print("mojodi shoma baraye enteghale vajh kafi nemibashd.")
    elif(requestType == 3):
       previous_password = input("lotfan ramze ghbali khod ra vared namayid: ")
       if(previous_password == passWord):
           new_password = input("lotfan ramze jadid khod ra vared namayid: ")
           new_password2 = input("lotfan ramze jadid khod ra mojadad vared namayid: ")
           if(new_password == new_password2):
               passWord = new_password2
               print("ramze shoma ba movafaghiyat taghir yaft.")
           else:
               print("ramze jadid vared shod sahih nemibashd.")    
       else:
        print("ramze ghabli vared shode sahih nemibashad.")    
else:
    print("ramze vared shode sahih nemibashad.")
 