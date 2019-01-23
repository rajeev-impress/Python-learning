test=[{'user':'pass'}]
print ("Original LIST",test)

key = input("Enter username: ")
val = input("Enter password: ")

dictt={}
dictt[key]=val
test.append(dictt)

print("Final LIST",test)
