import numpy as np
#newone
class newWeatherAnalyzer:
    def __init__(self,tempdata):
        self.tempdata = tempdata
    def getMinTemp(self):
        min_temp = np.min(self.tempdata)
        #print(min_temp)
        return min_temp
    def getMaxTemp(self):
        max_temp = np.max(self.tempdata) 
        #print(max_temp)
        return max_temp  
    def getMinTempAnnually(self):
        i = 0
        j = 0
        while j<= 29:
            list1 = []
            while i<= 358 and self.tempdata[i,0]== 1990+j:
                list1.append(self.tempdata[i,1])
                x = 1990+j
                i += 1
            print("The min temp for year",x,"is: ",np.min(list1))
            j += 1
        return ''    
    def getMaxTempAnnually(self):
        i = 0
        j = 0
        while j<= 29:
            list1 = []
            while i<= 358 and self.tempdata[i,0]== 1990+j:
                list1.append(self.tempdata[i,1])
                x = 1990+j
                i += 1
            print("The Max temp for year",x,"is: ",np.max(list1))
            j += 1
        return ''
    def getAvgSnowfall(self):
        i = 0
        y = 0
        a = []
        b = []
        while y<= 29:
            list1 = []
            while i<= 358 and self.tempdata[i,0] == 1990+y:
                list1.append(self.tempdata[i,1])
                i += 1
            a.append([np.average(list1)])
            b.append(1990+y)
            y += 1
        a = np.array(a)
        b = np.array(b)   
        l = np.column_stack((b,a))  
        
        return l
    def getAvgTempAnnually(self):
        i = 0
        j = 0
        while j<= 29:
            list1 = []
            list2 = []
            while i<358 and self.tempdata[i,0] == 1990+j:
                list1.append(self.tempdata[i,1])
                list2.append(self.tempdata[i,2])
                x = 1990+j
                i += 1
            max_temp = np.max(list1)
            min_temp = np.min(list2)
            avg = (max_temp+min_temp)/2
            print("The Average for the Year",x,"is:",avg)
            j +=1
        return ''                