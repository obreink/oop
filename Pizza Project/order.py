

class Pizza:

    _sizes: list[str] = ["Small","Medium","large","Large"]  #static variable to make pizza size available to all methods
    size_price: dict[str,float] ={
        "Small": 9.00,
        "medium": 12.45,
        "large": 15.44
        "Extra large": 18.00
    }
    topping_price: float  = 0.85





    def __init__(self,size: str,toppings : list[str]):
        """

        :param size:
        :param toppings:
        """


        if size.lower() in Pizza._sizes:
            self._size = size
        else:
            self._size= "small"  #set small as default pizza


        self.toppings = toppings
    @classmethod
    def validate_add_size(cls,new_size : str)-> bool:

        """


        Args:
            size(str) - the size to be validated
        :param new_size:
        :returns: True if the new size has been validated.   False if the size already exits

        """
        if new_size in Pizza._sizes:
            print("Pizza size already exits.")

        else:
            Pizza._sizes.append(new_size)






    def display(self)-> None:
        print(f"Pizza[toppings={self.toppings},size= {self._size}]")

    def get_pizza_size(self) -> str:

        return self._size


    def set_pizza_size(self,new_size : str) -> bool:
        if new_size.lower() in self._size:
            new_size = self._size

            return True
        else:  #if size is invalid
            return False


    def get_num_toppings(self) -> int :

        return len(self.toppings)


    def add_pizza_topping(self,topping: str)-> str | None:

        if topping in self.toppings:
            return "Pizza topping has already been added "

        else:
            self.toppings.append(topping)



    def remove_pizza_topping(self,matched_topping : str) -> bool:
        for topping in self.toppings:
            if topping == matched_topping:
                self.toppings.remove(topping)
                return True

            else:
                return  False


    def cal_price(self)- > float:

        return P












