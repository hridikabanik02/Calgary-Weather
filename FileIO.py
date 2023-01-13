import numpy as np
class FileIO:
    def __init__(self,filePath):
        self.filePath = filePath
        #self.filePath = r"C:\Users\pravas banik\Documents\UNIVERSITY\ENGG 233\Term Project\CalgaryWeather.csv"
        
    def read_data(self):
        data = np.loadtxt(self.filePath, delimiter = ',', skiprows=1,usecols=(0,1,2,3,4),dtype=np.float)
        self.dataTable = data
        return self.dataTable
