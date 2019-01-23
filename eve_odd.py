#my_list = [2,3,4,5,6,8,10]
my_list = input("ENTER YOUR LIST ")
my_list=list(my_list)
print(type(my_list))
print "MY ORIGINAL LIST IS" ,my_list
for i in range(len(my_list)):
    if ((my_list[i] % 2) == 0 ):
        print( str(my_list[i]) + " -->element is even")
        print('TESTING')
    else:
        print( str(my_list[i])+" -->element is ODD")
             
          
