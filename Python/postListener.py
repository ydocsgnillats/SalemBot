import bot
import praw
import sys
import time


subreddits = []
reddit = bot.reddit
username=reddit.config.custom['username']

class PostListener(bot.Bot):

    def __init__(self, subreddit = all):
        subreddits.append(subreddit)

    def listen(self):   #subreddit to listen to by user input
        firstPost = True
        old = []

        while True:
            try:
                for s in subreddits:
                    for post in reddit.subreddit(s).new(limit=10):
                        if firstPost is True:
                            old.append(post.id)
                        if post.id not in old:
                            self.redditMessage(post)
                            old.append(post.id)

                time.sleep(5)
                firstPost = False

            except IndexError:
                print("No subreddits selected. Try adding some with the popSubreddits() command!") 

            except KeyboardInterrupt:
                print('\n')
                sys.exit(0)

            except Exception as e:
                print(e)
   
    def popSubreddits(self,*argv):
        global subreddits
        for arg in argv:
            if arg.sub_exists:
                subreddits.append(arg)
                print("Added: r/" + arg + " to subreddit array.")
            else:
                print("The subreddit " + arg + " does not exist.")

    def clearSubreddits(self):
        global subreddits
        subreddits = ""
        print("Subreddit list cleared.")

    def redditMessage(self, post):
        subject = 'New post in ' + str(post.subreddit)
        content = '[' + post.title + '](' + post.shortlink + ')'
        reddit.redditor(username).message(subject, content)
        print('New post! Link sent as message.')
