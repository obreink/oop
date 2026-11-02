class Rectangle:
    def __init__(self, length, width, colour="Blue"):
        self.length = length
        self.width = width
        self.colour = colour

    def display(self):
        print(f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]")

    def calc_area(self):
        return self.length * self.width





    def __str__(self) -> str:

        return f"{self.length}, {self.width} {self.colour}"



    def __repr__(self) -> str:
        return f"Rectangle[length ={self.length}  ,width ={self.width}, colour = {self.colour} ] "



    def __format__(self, format_spec: str, /) -> str:

        match format_spec:
            case "Area":
                return f"{self.length}  * {self.width}"



            case _:
                return self.__str__()


    def __eq__(self, other:object -> bool:









if __name__ == "__main__":
    rect1 = Rectangle(4.4, 2.2, "Red")

    print(f"Length: {rect1.length}")
    print(f"Width: {rect1.width}")
    print(f"Colour: {rect1.colour}")

    rect1.display()
    area = rect1.calc_area()
    print(f"The area of rect1 = {area}")