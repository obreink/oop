from zipfile import sizeCentralDir


class Pizza:

    #PART A
    size = "Medium"
    toppings = "Pineapple"









    def __init__(self,toppings,size= "Small"):

        self.toppings = toppings
        self._size = size

     # PART B
        if size in :
            self.__size = size

        else:
            self.__size = "small"    # set small to default

    def display(self):
        print(f"Pizza[toppings={self.toppings},size= {self.__size}]")

    def get_pizza_size(self):

        return self.__size


    def set_pizza_size(self):
        if self.__size == "Small":
            self.__size = size

        elif self.__size == "Medium":
            self.__size = "Medium"

        elif self.__size == "Large":
            self.__size = "Extra Large"


        else:
            return  False

    def get_num_toppings(self):

        topping_count = 0

        for topping in self.toppings:
            topping_count += 1
        return topping_count

    def add_pizza_topping(self,topping):












