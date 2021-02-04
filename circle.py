class Circle:
    radius = 0.0

    def __init__(self, new_radius):
        self.radius = new_radius


    def calculate_area(self):
        print("Area equals" +   self.radius * 3.14 ** 2)


    def calculate_perimeter(self):
        c = 2 * 3.14 * self.radius
        print("Perimeter equals" + self.radius + c)