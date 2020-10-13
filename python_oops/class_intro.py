class Dog:
    #Class attribute
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self,sound):
        return f"{self.name} says {sound}"


class Bread1(Dog):
    def speak(self,sound="default"):
        return super().speak(sound)


a=Dog("a",1)
print(a.species)
print(a)
print(a.speak("how are you?"))

Dog.species= "changed" 

b=Bread1("b",2)
print(b)
print(b.speak())


print(b.species)

print(Dog.species)