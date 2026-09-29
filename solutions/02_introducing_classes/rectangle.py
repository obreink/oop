from shapes import Rectangle






def find_greatest_area(rect_list):

    max_area = 1
    biggest = None

    for rect in rect_list():
        if rect.calc_area() > max_area:
            max_area = rect.calc_area
            biggest = rect

def find_smallest_width(rect_list):

    smallest = rect_list[0].
    smallest = smallest.width

    for rect in rect_list:
        if rect.width < smallest.width


def find_red_rectangle():


if __name__ == "__main__":
    rectangles= []

    for i in range(5):
        rect = Rectangle()

        for i in range(5):
            length = float(input(f"input rectangle length   {(i+1)} :"))
            width = float(input(f"input width length  {(i+1)} : " ))
            colour = input(f"Enter colour of rectange {(i+1)}:" )

            rect.length = length
            rect.width = width
            rect.colour = colour

            rectangles.append(rect)

            # save user data into the list

            max_rect = find_greatest_area(rectangles)

            if max_rect is not None:
                max_rect.display()









































