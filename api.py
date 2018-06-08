class api:
    # todo: make url string more modular
    # ---config---#
    app = 3
    apiroot = "https://devrant.com/api"
    import urllib.request as req
    import json
    def get_rants(self):
        with self.req.urlopen(self.apiroot + "/devrant/rants"+ "?app="+str(self.app)) as f:
            i = self.json.loads(f.read().decode())
        return i
    def get_rant(self,id):
        with self.req.urlopen(self.apiroot + "/devrant/rants/"+ id + "?app="+str(self.app)) as f:
            i = self.json.loads(f.read().decode())
        return i

    def get_user(self,id):
        with self.req.urlopen(self.apiroot + "/users/"+ str(id) + "?app="+str(self.app)) as f:
            i = self.json.loads(f.read().decode())
        return i





