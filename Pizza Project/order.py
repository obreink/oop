

class Pizza:

    _sizes = ["Small","Medium","large","Large"]  #static variable to make pizza size available to all methods


    def __init__(self,size,toppings):


        if size.lower() in Pizza._sizes:
            self._size = size
        else:
            self._size= "small"  #set small as default pizza

        self.toppings = toppings




    def display(self):
        print(f"Pizza[toppings={self.toppings},size= {self._size}]")

    def get_pizza_size(self):

        return self._size


    def set_pizza_size(self,new_pizza_size):
        if new_pizza_size.lower() in self._size:



            return True
        else:  #if size is invalid
            return False


    def get_num_toppings(self):


        topping_count = 0

        for topping in self.toppings:
            topping_count +=1
        return topping_count

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













