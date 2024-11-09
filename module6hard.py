class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self._color = None
        self.set_color(color)
        
        if len(sides) != self.sides_count:
            sides = [1 for _ in range(self.sides_count)]
            
        self._sides = list(sides)
        self.filled = False

    def get_color(self):
        return self._color

    def set_color(self, color):
        if self.is_valid_color(color):
            self._color = color

    def is_valid_color(self, color):
        r, g, b = color
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])

    def get_sides(self):
        return self._sides[:]

    def set_sides(self, *new_sides):
        if self.is_valid_sides(new_sides):
            self._sides = new_sides

    def is_valid_sides(self, new_sides):
        return (
            len(new_sides) == self.sides_count
            and all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def length(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def radius(self):
        return self.length() / (2 * 3.14159)

    def square(self):
        return 3.14159 * self.radius() ** 2

    def length(self):
        return self._sides[0]


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def square(self):
        a, b, c = self._sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def volume(self):
        edge_length = self._sides[0]
        return edge_length ** 3

    def set_sides(self, *new_sides):
        if self.is_valid_sides(new_sides):
            self._sides = [new_sides[0]] * self.sides_count

# Примеры использования:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print("Color of circle:", circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print("Color of cube:", cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print("Sides of cube:", cube1.get_sides())
circle1.set_sides(15)  # Изменится
print("Sides of circle:", circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print("Length of circle:", circle1.length())

# Проверка объёма (куба):
print("Volume of cube:", cube1.volume())
