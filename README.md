# FacebookWebBot

=======================

A simple library to automatize facebook without the official API
All the functions are made scrapping and parsing mbasic.facebook.com

## Available functions:

    Login
    Logout
	Post in your timeline
	Message friends
	Get post in a facebook group
	Post in a facebook group
	Comment in a post
	Get the members of a facebook group
	Send friend request
	Send message to any person
	Get all post from a profile/fanpage
	Send group request
	Get number of likes and coments in a post
	Post in a fanpage/friend timeline
    
## Basic usage example:

```
from FacebookWebBot import *
bot=FacebookBot()
bot.set_page_load_timeout(10)
bot.login("your@email.com","yourpassword")
allpost=bot.getPostInProfile("https://mbasic.facebook.com/your-gf-profile",deep=50)
for p in allpost:
	print(p)
```
## Installing
pip install FacebookWebBot
## Know issues:

    * Can't post images because PhantomJS limitations.

## Dependencies:

    * Python 3.4

    * Selenium

    * PhantomJS
