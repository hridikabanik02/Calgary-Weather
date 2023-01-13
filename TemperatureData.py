from Date import Date
class TemperatureData():
    def __init__(self,Month,Year,maxTemp,minTemp,snowfall):
        self.date= Date(Month,Year)
        self.maxTemp = maxTemp
        self.minTemp = minTemp
        self.snowfall = snowfall
    def getmax(self):
        return (self.maxTemp)
    def getmin(self):
        return (self.minTemp)
    def getmonth(self):
        m = self.date.getmonth()
        return m
    def getyear(self):
        y = self.date.getyear()
        return y
    def getsnowfall(self):
        return (self.snowfall)