import json


def addUser(name, sub):
    with open("data\\users.json", "r+") as json_file:
        data = json.load(json_file)
        newUser = {
            'Name': name,
            'Subreddit': sub
        }
        data['users'].append(newUser)
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()


def checkUser(name):
    jsonFile = open("data\\users.json", "r+")
    data = json.load(jsonFile)
    for d in data['users']:
        if d['Name'] == name:
            return True
        else: 
            return False
