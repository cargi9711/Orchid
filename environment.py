class Environment:
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    def describe(self):
        return f"Environment at {self.temperature}°C with {self.humidity}% humidity."
