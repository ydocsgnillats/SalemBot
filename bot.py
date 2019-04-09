import praw
import config
import time
import re

#logging in to reddit using information from config.py
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent="Salembot v0.1",
                     username=config.username,
                     password=config.password)

subreddits = ['salemwitchtrials', 'footfedoras']
pos = 0
errors = 0

title = "Witch Test Post"
url = "https://imgur.com/a/xa6CM5g"

def post():
    global subreddits
    global pos
    global errors

    #try posting on subreddits listed
    try:
        subreddit = reddit.subreddit(subreddits[pos])
        subreddit.submit(title, url = url)
        print("Posted to " + subreddits[pos] + "\n")
        pos = pos+1

        if (pos <= len(subreddits) - 1):
            post()
        else:
            print ("Done")
    
    #catch if posting too often, delay post by the necessary time
    except praw.exceptions.APIException as e:
        if (e.error_type == "RATELIMIT"):
            delay = re.search("(%d) minutes", e.message)
            if delay:
                delay_seconds = float(int(delay.group(1)) * 60)
                time.sleep(delay_seconds)
                post()
            else: 
                delay = re.search("(%d) seconds", e.message)
                delay_seconds = float(delay.group(1))
                time.sleep(delay_seconds)
                post()

    except: 
        errors = errors+1
        if(errors >5):
            print("Program Crashed")

post()
