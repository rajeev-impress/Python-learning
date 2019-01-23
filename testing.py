data = {"people": [{"name": "Scott", "website": "stackabuse.com", "from": "Nebraska"}, {"name": "Larry", "website": "google.com", "from": "Michigan"}, {"name": "Tim", "website": "apple.com", "from": "Alabama"}]}

for p in data['people']:
        #print (p)
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
