class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
rectangle1 = Rectangle(2, 3)
rectangle2 = Rectangle(30, 2)
print(
    f"Параметры первого прямоугольника: "
    f"Площадь = {rectangle1.area()} "
    f"Периметр = {rectangle1.perimeter()} "
)
print(
    f"Параметры второго прямоугольника: "
    f"Площадь = {rectangle2.area()} "
    f"Периметр = {rectangle2.perimeter()} "
)
