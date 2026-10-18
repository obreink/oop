

class Pizza:

    _sizes = ["Small","Medium","large","Large"]  #static variable to make pizza size available to all methods
    size_price ={
        "Small": 9.00,
        "medium": 12.45,
        "large": 15.44
        "Extra large": 18.00
    }
    topping_price = 0.85





    def __init__(self,size,toppings):


        if size.lower() in Pizza._sizes:
            self._size = size
        else:
            self._size= "small"  #set small as default pizza


        self.toppings = toppings
    @classmethod
    def validate_add_size(cls,new_size):
        if new_size in cls.Pizza:
            print("Pizza size already exits.")

        else:
            cls.Pizza.append(new_size)






    def display(self):
        print(f"Pizza[toppings={self.toppings},size= {self._size}]")

    def get_pizza_size(self):

        return self._size


    def set_pizza_size(self,new_size):
        if new_size.lower() in self._size:
            new_size = self._size

            return True
        else:  #if size is invalid
            return False


    def get_num_toppings(self):

        return len(self.toppings)


    def add_pizza_topping(self,topping):

        if topping in self.toppings:
            return "Pizza topping has already been added "

        else:
            self.toppings.append(topping)



    def remove_pizza_topping(self,matched_topping):
        for topping in self.toppings:
            if topping == matched_topping:
                self.toppings.remove(topping)
                return True

            else:
                return  False


    def cal_price(self):
        return












