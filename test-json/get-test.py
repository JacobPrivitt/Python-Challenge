import json
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as f:
        return json.load(f)

myObj = getJSON('test.json')
print(myObj.get ("Hello"))

