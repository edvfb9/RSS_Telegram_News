# RSS_Telegram_News
I wrote this little script for me to constantly run on a raspberry pi.

It basicly takes all the RSS Feeds which are stored in the *config.txt* file and sends them via the Telegram bot.

### Keyword and tag filter

But because some rss feeds are also posting stuff which is of no interest to me, i also build in a function to filter for certain tags. If no tags are handed in it sends all posts from the rss feed. Furthermore i added the feature to filter for keywords in the title. Note that if you use keywords and tags there has to be an overlap where at least one tag and one keyword is true. If you want to get around this at the moment you have to add the same source twice in the config.

### Multiple User Support

I also added a feature which enables multiple users to subscribe to the RSS News Bot on their own and receive all the news as well. This is achieved by storing all the chat ids in an sqlite database which is managed in the Chat_Id.py file. To subscribe to the RSS Bot one simply has to text a random message to the bot. To unsubscribe from the RSS Bot one has to simply send a message containing "unsubscribe".

### TO-DO: 
    - Option to change the database directory and file name in the config.txt file