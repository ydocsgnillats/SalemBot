import praw
import time
import sys
import re
import json
import info
import postListener
from prawcore import NotFound

reddit = praw.Reddit('bot2',user_agent='Salem Bot V1.0')

pos = 0
errors = 0
title = "Witch Test Post"
url = "https://imgur.com/a/xa6CM5g"

class Bot:

    def outreach(self, sub_sent_from):
        sub = reddit.subreddit('all')
        lim = 10
        key = input("Search Term: ")
        
        for i in sub.search(key, limit=lim):
            user = i.author.name
            message = ('Hey! I\'m a bot here to tell you about reddit.com/r/' + sub_sent_from + '\nWe are currently looking for more content and interest and we\'d love it if you checked us out! Additionally, feel free to message this bot if you feel like you would be a good fit to help moderate the sub! \n Thank you, \n SalemBot')
            reddit.redditor(user).message(sub_sent_from + " invite", message, 
                            from_subreddit= sub_sent_from)
            print("Sent a message to " + user)

    def post(self, sub):
        global errors
        #try posting on subreddits listed
        try:
            subreddit = reddit.subreddit(sub)
            subreddit.submit(title, url = url)
            print("Posted to r/" + sub)
            pritn("Done.")
        
        #catch if posting too often, delay post by the necessary time
        except praw.exceptions.APIException as e:
            if (e.error_type == "RATELIMIT"):
                delay = re.search("(%d) minutes", e.message)
                if delay:
                    delay_seconds = float(int(delay.group(1)) * 60)
                    time.sleep(delay_seconds)
                    self.post(sub)
                else: 
                    delay = re.search("(%d) seconds", e.message)
                    delay_seconds = float(delay.group(1))
                    time.sleep(delay_seconds)
                    self.post(sub)

        except: 
            errors = errors+1
            if(errors >5):
                print("Program Crashed")

    def sub_exists(self, sub):
        exists = True
        try:
            reddit.subreddits.search_by_name(sub, exact=True)  
        except NotFound:
            exists = False
        return exists

def main():
    
    print("Loading...")
    #info.addUser('salem_bot', 'salemwitchtrials')
    #info.checkUser('salem_bot')
    p = postListener.PostListener('watchuraffle')
    p.listen()
    
if __name__ == '__main__': main() #runs main only if this file is ran as the main program
        



