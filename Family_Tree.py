class FamilyMember:
    def __init__(self,eyecolour,height_cm):
        self.eyecolour=eyecolour
        self.height_cm=height_cm

    def show_traits(self):
        print("Eye colour: ", self.eyecolour)
        print("Height in cm: ",self.height_cm)

class Kid(FamilyMember):
    def __init__(self,name,age,eyecolour,height_cm):
        self.name=name
        self.age=age
        super().__init__(eyecolour,height_cm)

    def show_traits(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        super().show_traits()
    
    def favourite_hobby(self,hobby):
        print(self.name,"loves",hobby)
 
child=Kid("Lucas",10,"brown",149)
child.show_traits()
child.favourite_hobby("painting")

print("Is Kid a subclass of FamilyMember? ",issubclass(Kid, FamilyMember))