from FileIO import FileIO
from newWeatherAnalyzer import newWeatherAnalyzer
from TemperatureData import TemperatureData
import numpy as np
def main():

    file = r"C:\Users\pravas banik\Documents\UNIVERSITY\ENGG 233\Term Project\CalgaryWeather.csv"
    data = FileIO(file)
    data = data.read_data()
    tempdata = TemperatureData(data[:,1],data[:,0],data[:,2],data[:,3],data[:,4])
    print("""
    1. Get Minimum Temperature of 1990-2019
    2.Get Maximum Temperature of 1990-2019
    3.Get Minimum Temperature of 1990-2019 Annually
    4.Get Maximum Temperature of 1990-2019 Annually
    5.Get Average Snowfall between 1990-2019 Annually
    6.Get Average Average Temperature between 1990-2019 Anually
    7.Linchart Minimum Temperature of 1990-2019 Annually
    8.Linechart Maximum Temperature of 1990-2019 Annually
    9.BarChart Average Snowfall between 1990-2019 Annually
    10.BarChart Average Temperature between 1990-2019 Annually
    """)
    sec = int(input("Enter section between 1 and 10: "))
    while sec < 1 or sec >10:
        sec = int(input("Invalid input! Choose a section between 1 and 10: "))
    
    if sec == 1:
        mintemplist = tempdata.getmin()
        mini = newWeatherAnalyzer(mintemplist)
        mini = mini.getMinTemp()
        print("The Minimum Temperature",mini)
    if sec == 2:
        maxtemplist = tempdata.getmax()
        max = newWeatherAnalyzer(maxtemplist)
        max = max.getMaxTemp()
        print("The Maximum Temperature is",max)
    
    if sec == 3:
        getyear = tempdata.getyear()
        mintemplist = tempdata.getmin()
        make = np.array(list(zip(getyear,mintemplist)))
        make = newWeatherAnalyzer(make)
        makemin = make.getMinTempAnnually()
        print(makemin)
    if sec == 4:
        getyear = tempdata.getyear()
        maxtemplist = tempdata.getmax()
        arr2 = np.array(list(zip(getyear,maxtemplist)))
        arr2 = newWeatherAnalyzer(arr2)
        arr = arr2.getMaxTempAnnually()
        print(arr)
    if sec == 5:
        getyear = tempdata.getyear()
        snow = tempdata.getsnowfall()
        arr3 = np.array(list(zip(getyear,snow)))
        arr3 = newWeatherAnalyzer(arr3)
        arr = arr3.getAvgSnowfall()
        print("The Average Snowfalls are: ")
        print(arr)
    if sec == 6:
        getyear = tempdata.getyear()
        maxtemplist = tempdata.getmax()
        mintemplist = tempdata.getmin()
        avg = np.array(list(zip(getyear,maxtemplist,mintemplist)))
        avg = newWeatherAnalyzer(avg)
        avg = avg.getAvgTempAnnually()
        print(avg)
    #if sec == 7:
    #if sec == 8:
    # if sec == 9:
    # if sec == 10:    
if __name__ == "__main__":
    main()