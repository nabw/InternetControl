
class Twitter:

    def __init__(self):
        self.cfg = {"consumer_key"        : "", 
                    "consumer_secret"     : "",
                    "access_token"        : "",
                    "access_token_secret" : "" 
                    }    

    def get_api(self, cfg):
        import tweepy
        auth = tweepy.OAuthHandler(self.cfg['consumer_key'], self.cfg['consumer_secret'])
        auth.set_access_token(self.cfg['access_token'], self.cfg['access_token_secret'])
        return tweepy.API(auth)

    def tweet(self, msg):
        api = self.get_api(self.cfg)
        status = api.update_status(status=msg) 
        
