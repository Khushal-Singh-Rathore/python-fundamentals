class Flyer:
    def fly(self): print("Flying...")

class Swimer:
    def swin(self):print("Swim...")

class Duck(Flyer,Swimer):
    pass

d = Duck()

d.fly()
d.swin()