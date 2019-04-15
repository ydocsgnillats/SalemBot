import json


def addUser(name, sub):
    username = name
    subreddit = sub
    if checkUser(name) == False:
        with open("files\\users.json", "r+") as json_file:
            data = json.load(json_file)
            newUser = {
                'Name': username,
                'Subreddit': subreddit
            }
            data['users'].append(newUser)
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
    else: 
        with open("files\\users.json", "r+") as json_file:
            data = json.load(json_file)
            for d in data['users']:
                if d['Name'] == name:
                    d['Subreddit'].append(subreddit)
                    json_file.seek(0)
                    json.dump(data, json_file, indent=4)
                    json_file.truncate()
                else:
                    return("There was a problem adding this subreddit to " + username)


def checkUser(name):
    jsonFile = open("files\\users.json", "r+")
    data = json.load(jsonFile)
    for d in data['users']:
        if d['Name'] == name:
            message = (name + " is listed in users.json from the subreddit r/" + d['Subreddit'])
            return True
        else: 
            message = (name + " was not found listed in users.json")
            return False
    print(message)