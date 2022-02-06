class Config(object):
    def __init__(self,cycletime,ratio):
        self.cycletime=cycletime
        self.ratio=ratio
        self.score=0
        self.totalscore=0
        self.cycles=0
        self.averagescore=0
    def ComputeAverage(self):
        self.averagescore=self.totalscore/self.cycles