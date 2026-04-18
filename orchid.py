class Orchid:
    def __init__(self, name, color, origin):
        self.name = name
        self.color = color
        self.origin = origin

    def bloom(self):
        return f"{self.name} blooms beautifully in {self.color} color."

    def __str__(self):
        return f"{self.name} | Color: {self.color} | Origin: {self.origin}"
