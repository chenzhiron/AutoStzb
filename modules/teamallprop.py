class StTeamAllProp:
    def __init__(self):
        self.data = {}
    def initialize(self):
        self.data["besiegemain"] = {
          "state": False
        }
        self.data["basiegedestory"] = {
            "state": False
        }
        self.data["exploit"] = {
          "state": False
        }
        self.data["enemymain"] = {
          "state": False
        }
        self.data["battledestory"] = {
          "state": False
        }
        self.data["myfight"] = {
          "state": False
        }
    def updatecheckbox(self, obj, k, v):
        if len(v) == 0:
          v = False
        else:
          v = True
        self.data[obj][k] = v
    def update(self, obj, k, v):
        self.data[obj][k] = v
    
    def __repr__(self):
        return f"StTeamAllProp(data={self.data})"

stteamprop = StTeamAllProp()
stteamprop.initialize()
print(stteamprop)
