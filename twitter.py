
from SocialMedia import *

class Twitter(SocialMedia):

    def __init__(self,tweet):
        super().__init__(Twitter)
        self.tweet = tweet
        self.Tweets = []
    
    def Validate(self):
        if len(self.tweet) >= 280 :
            return("Your tweet is illigal.")
        else :
            self.Tweets.append(self.tweet)
            return("Your tweet has successfully added.")
        
    def getTweets(self):
        return(self.Tweets)


t1 = Twitter("Hello buddy! whats up")
print(t1.Validate())
print(t1.getTweets())