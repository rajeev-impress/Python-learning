a = ['raj','sham','ritu'] 
print(list(enumerate(a)))
exam = dict (list(enumerate(a)))
print (exam)

### nested dict###

Dict = dict({1: 'Geeks', 2: 'For', 3:dict (list(enumerate(a)))})
print (Dict)

###dump to json####

import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
