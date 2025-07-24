# birds.py
class Eagle:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def speak(self):
        return f"{self.name} says Screech!"

    def info(self):
        return f"{self.name} is an eagle with a wingspan of {self.wingspan} meters."

