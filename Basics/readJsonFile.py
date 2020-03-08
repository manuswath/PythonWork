import json
config = json.loads(open('user.json').read())
print (config)
print (config["username"])
print(config["password"])