class Rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l* self.b

    def param(self):
        return self.l* self.b

obj=Rect(50,20)
print(obj.area())
print(obj.param())