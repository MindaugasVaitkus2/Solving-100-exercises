import json
from pprint import pprint

with open ('company1.json', 'r') as f:
    data = json.load(f)
    #pprint (data)
data['employees'].append(dict(firstName =  'Albert', lastName = 'Bert'))
with open ('company1.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4)

# how he did
# with open("company1.json", "r+") as file:
#     d = json.loads(file.read())
#     d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
#     file.seek(0)
#     json.dump(d, file, indent=4, sort_keys=True)
#     file.truncate()