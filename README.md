# SalemBot

This is a reddit bot that will have new features tested out/added to it over time.



### Requirements:

Praw:
> pip install praw 
[Documentation](https://praw.readthedocs.io)



### Setup:

> Log into reddit with the profile you would like to use the bot on (or make a profile for the bot)

> Create an [application here](www.reddit.com/prefs/apps)

> Set the information in config.py to your username/password and bot id/secret

> For any additional help setting up your own bot, [check this out](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)



### Features:

| Function      | Description           | Command |
| :-------------: |:-------------:| :-----:|
| Outreach | Scans r/all for a key phrase in a post, invites author of the post to a subreddit by sending a message | ------ |
| Post | Posts a specific link and title to a subreddit(s) | ----- |
| PostListen | Listens for new posts to a subreddit(s). Sends the user a message on reddit with link to new post | ----- |