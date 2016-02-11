
class Twitter:

    def __init__(self):
        self.cfg = {"consumer_key"        : "K16Z7pjsRbsJNmBDkJRAwH7GU", 
                    "consumer_secret"     : "OfOjkoZybTmhicGJKxb9dBwhfEOXl4Ei5yvDzEsdChrLWEtIpJ",
                    "access_token"        : "255150642-3tl3r5oOCkI9XvakfJpTTOJ9OjTDVVzQMPl2EYTq",
                    "access_token_secret" : "4Xr82179Cb3nhZgs9rC3ltgepI7s2h1mpO3aL5dQHnkUL" 
                    }    

    def get_api(self, cfg):
        import tweepy
        auth = tweepy.OAuthHandler(self.cfg['consumer_key'], self.cfg['consumer_secret'])
        auth.set_access_token(self.cfg['access_token'], self.cfg['access_token_secret'])
        return tweepy.API(auth)

    def tweet(self, msg):
        api = self.get_api(self.cfg)
        status = api.update_status(status=msg) 
        
