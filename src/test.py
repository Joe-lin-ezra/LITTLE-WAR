import json

dic = {'event':1, 'argu':0}

print(dic, type(dic))

dic = json.dumps(dic)

print(dic, type(dic))

json.loads()
