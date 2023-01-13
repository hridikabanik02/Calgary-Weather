import matplotlib.pyplot as pyplot
import numpy as np
class Chart:
    def __init__(self,x,y,title,x_label,y_label):
        self.x = x
        self.y = y
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def drawLineChart(self,x,y,title,x_label,y_label):
       
        pyplot.title(self.title)
        pyplot.ylabel(self.y_label)
        pyplot.xlabel(self.x_label)
        pyplot.plot(self.x,self.y, marker = 'o')
        pyplot.show()
    def drawBarChart(self,x,y,title,x_label,y_label):
        
        pyplot.title(self.title)
        pyplot.ylabel(self.y_label)
        pyplot.xlabel(self.x_label)
        pyplot.bar(self.x, self.y)
        pyplot.show()



