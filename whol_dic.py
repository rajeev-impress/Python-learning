def main():
    
    # Dictionary of strings and ints
    wordFreqDic = {
        "Hello": 56,
        "at" : 23 ,
        "test" : 43,
        "this" : 43
        }
    
    
    print("Original Dict : " , wordFreqDic)
    

    '''
    Adding a new key value pair in dictionary
    '''

    print("Appending key value pair in dictionary")
        
    # Adding a new key value pair
    wordFreqDic.update( {'before' : 23} )
    
    print("Modified Dict : ")
    for (key, value) in wordFreqDic.items() :
        print(key , " :: ", value )
    
    # Adding a new key value pair
    wordFreqDic.update(test = 'value' )
    
    print("Modified Dict : ")
    for (key, value) in wordFreqDic.items() :
        print(key , " :: ", value )

    '''
    Updating value of existing key in dictionary
    '''
    print("Updating values in dictionary")
    
    # Updating existing key's value
    wordFreqDic.update(Hello = 99 )
    
    print("Modified Dict : ")
    for (key, value) in wordFreqDic.items() :
        print(key , " :: ", value )


    
    '''
    Adding multiple key value pair in dictionary
    '''
    print("Append list of tuples in dictionary")
    
    # Adding a List of tuples to the existing dictionary
    wordFreqDic.update([ ('where', 4) , ('who', 5) , ('why', 6) , ('before' , 20)] )
    
    print("Modified Dict : ")
    for (key, value) in wordFreqDic.items() :
        print(key , " :: ", value )


    print("Append one dictionary to another dictionary")    
    
    # Two dictionaries
    dict1 = {
        "Hello": 56,
        "at" : 23 ,
        "test" : 43,
        "this" : 43
        }
    dict2 = { 'where' : 4 ,
         'who' : 5 ,
         'why': 6 ,
         'this' : 20 
         }
    
   
    # Adding elements from dict2 to dict1
    dict1.update( dict2 )
    
    print("Modified Dict1 : ")
    for (key, value) in dict1.items() :
        print(key , " :: ", value )


if __name__ == '__main__':
    main()
