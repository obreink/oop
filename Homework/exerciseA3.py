#Add a constructor to your Rectangle class (from the previous worksheet) that takes in the length, width and colour of
#a Rectangle. The colour attribute should have a default value of “Blue”. The length and width attributes should not
#have any default values.

class Rectangle:
    def __init__(self,length,width,colour="blue"):
        self.length=length
        self.width=width
        self.colour=colour

    def display(self):
        print(self.length,self.width,self.colour)
if __name__=="__main__":
    rectangle=Rectangle(10,20)
    rectangle2=Rectangle(10,20,colour="red")
    rectangle.display()




