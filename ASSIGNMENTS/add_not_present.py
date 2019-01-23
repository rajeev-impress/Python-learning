server = []
while True:
 sname = input("Please enter any server ")
 if sname in server:
     print(sname,"Server Exist in our inventory")
 else:
     print(sname,"Server not found")
     print("to add --",sname,"enter 'y': or exit (press any other key:)")
     i = input()
     if i == 'y' : 
         server.append(sname)
         print("\nCurrent server list:",server)
     else :    
       print("Do come back again, thanks!!")    
       break 

