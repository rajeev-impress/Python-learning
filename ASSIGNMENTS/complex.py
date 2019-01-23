serverusage = [{ "servername" : "BL0123", "cpu" : {10,20,30} } , { "servername" : "BL0234", "cpu" : (70,10) }, { "servername" : "BL0256", "cpu" : 80 }, { "servername" : "BL0981", "cpu" : [85] } ]

for item in serverusage:
    for k,v in item.items(): 
        if k == 'cpu': 
            print(v,"-->",type(v))
