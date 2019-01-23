test=[]
print ("\nOriginal LIST -->",test)
i = 'y'
while i== 'y':

    key = input("Enter username: ")
    val = input("Enter password: ")
    test.append(dict([(key,val)]))
    print("Final LIST",test)
    i= input("\nEnter y if you want to insert KV: ")
