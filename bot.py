import praw
import config
import time
import sys
import re

#logging in to reddit using information from config.py
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent="Salembot v0.1",
                     username=config.username,
                     password=config.password)

subreddits = ['salemwitchtrials']
username=config.username
pos = 0
errors = 0

title = "Witch Test Post"
url = "https://imgur.com/a/xa6CM5g"

def outreach(key):
    sub = reddit.subreddit('all')
    message_limit = 1
    
    while message_limit <=5:
        for i in sub.search(key, limit=100):
            user = i.author.name
            message = ('Hey! I\'m a bot here to tell you about reddit.com/r/' + str(subreddits) + '\nWe are currently looking for more content and interest and we\'d love it if you checked us out! Additionally, feel free to message this bot if you feel like you would be a good fit to help moderate the sub! \n Thank you, \n SalemBot')
            reddit.redditor(user).message('Salem Witch Trials', message, 
                                        from_subreddit='salemwitchtrials')
            message_limit+=1
            print("Sent a message to " + user + "\n")

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

def postListen():   #subreddit to listen to by user input
    firstPost = True
    old = []

    while True:
        try:
            for s in subreddits:
                for post in reddit.subreddit(s).new(limit=10):
                    if firstPost is True:
                        old.append(post.id)
                    if post.id not in old:
                        subject = 'New post in ' + str(post.subreddit)
                        content = '[' + post.title + '](' + post.shortlink + ')'
                        reddit.redditor(username).message(subject, content)
                        print('New post! Link sent as message.')
                        old.append(post.id)

            time.sleep(5)
            firstPost = False

        except KeyboardInterrupt:
            print('\n')
            sys.exit(0)

        except Exception as e:
            print(e)

def popSubreddits(*argv):
    global subreddits
    for arg in argv:
        subreddits.append(arg)
        print("Added: r/" + arg + " to subreddit array.")

if __name__ == '__main__':  #performs tasks below only if this file is ran as the main program
    
    print("Loading...")
    #postListen()
    #popSubreddits('askreddit', 'watches', 'diwhy') #change to take user input(even multiple inputs)
    #outreach('witch') #change to take user input(with multiple words/spaces)



#               TODO    
#       add json functionality for keeping track of users, subreddits, etc?
#       create a main file to run these from with a better UI and commands
