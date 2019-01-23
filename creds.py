a = [{"user":'rajeev',"password":'python123'},{"user":'admin',"password":'admin123'}]

val = input("Please enter user: ")
for i in range(len(a)):
        if val == a[i]["user"]:
            print(val ,'is valid user \n')
            pas = input('please enter password:')
            if pas == a[i]["password"]:
                print("Success FULL Verification")
                break
            else:
                if i == len(a)-1 :
                  print("Wrong password")
        else:
            if i == len(a)-1:
             print(val ,'\nis Invalid user')
