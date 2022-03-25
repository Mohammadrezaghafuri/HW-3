
from SocialMedia import *


class instagram(SocialMedia):
    def __init__(self,post):
        super().__init__(instagram)
        self.post = post
        self.Posts = []
 

    def validate(self):
        if len(self.post) >= 2200:
            return('your post is illigal')
        else:
            self.Posts.append(self.post)
            return('Your post has successfully added.')

    def getPosts(self):
        return(self.Posts)    


i1 = instagram('Hello buddy! whats up')
print(i1.validate())
print(i1.getPosts())     