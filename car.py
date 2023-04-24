class Cars(object):
    def __init__ (self, name, color, model):
        self.name = name
        self.model = model
        self.color = color
    
    def display(self):
        print(self.name, self.color, self.model)
Car1 = Cars("Tesla","X", "Black")
Car2 = Cars("Audi", "Q7", "White")
Car1.display()
Car2.display()
Car2.color = "Red"
print(Car2.color)
