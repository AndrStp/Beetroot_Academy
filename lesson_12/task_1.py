# Method overloading.

# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, 
# and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, 
# while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter. 


class Animal:
    
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
    
    def talk(self) -> None:
        print('Sound')


class Dog(Animal):

    def __init__(self, name, color) -> None:
        super().__init__(name, color)
    
    def talk(self) -> None:
        print('woof woof')


class Cat(Animal):

    def __init__(self, name, color) -> None:
        super().__init__(name, color)

    def talk(self) -> None:
        print('meow meow')


def talk_func(animal: object) -> None:
    animal.talk()


unknown_spicie = Animal('Alien', 'black')
dog = Dog('Jack', 'black')
cat = Cat('Marty', 'white')

talk_func(unknown_spicie)
talk_func(dog)
talk_func(cat)
