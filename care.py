class OrchidCare:
    def __init__(self, light, water, humidity):
        self.light = light
        self.water = water
        self.humidity = humidity

    def instructions(self):
        return f"Light: {self.light}, Water: {self.water}, Humidity: {self.humidity}%"
