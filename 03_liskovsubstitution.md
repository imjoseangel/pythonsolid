"""
Liskov Substitution Principle

A sub-class must be substitutable for its super-class. When extending a class,
remember that you should be able to pass objects of the subclass in place of
objects of the parent class without breaking the client code. The aim of this
principle is to ascertain that a sub-class can assume the place of its
super-class without errors. If the code finds itself checking the type of class
then, it must have violated this principle.

Let’s use our Animal example.
"""


DEFAULT_LION_LEG_COUNT = 4
DEFAULT_MOUSE_LEG_COUNT = 4
DEFAULT_SNAKE_LEG_COUNT = 0


class Animal:
    pass


def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(DEFAULT_LION_LEG_COUNT)
        elif isinstance(animal, Mouse):
            print(DEFAULT_MOUSE_LEG_COUNT)
        elif isinstance(animal, Snake):
            print(DEFAULT_SNAKE_LEG_COUNT)


class Lion(Animal):
    pass


class Mouse(Animal):
    pass


class Snake(Animal):
    pass


animals = [
    Lion(),
    Mouse(),
    Snake()
]


animal_leg_count(animals)

"""
To make this function follow the Liskov Substitution principle, we will follow
this Liskov Substitution Principle requirements postulated by Steve Fenton:

If the super-class (Animal) has a method that accepts a super-class type
(Animal) parameter, its sub-class(Snake) should accept as argument a
super-class type (Animal type) or sub-class type(Snake type). If the
super-class returns a super-class type (Animal), Its sub-class should return a
super-class type (Animal type) or sub-class type(Snake). Now, we can
re-implement animal_leg_count function:
"""

DEFAULT_LION_LEG_COUNT = 4
DEFAULT_MOUSE_LEG_COUNT = 4
DEFAULT_SNAKE_LEG_COUNT = 0


def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.get_legs_count())


"""
The animal_leg_count function cares less the type of Animal passed, it just
calls the leg_count method.  All it knows is that the parameter must be of an
Animal type, either the Animal class or its sub-class.

The Animal class now have to implement/define a get_legs_count method. And its
sub-classes have to implement the get_legs_count method:
"""


class Animal:
    def get_legs_count(self):
        pass


class Lion(Animal):
    def get_legs_count(self):
        return DEFAULT_LION_LEG_COUNT


class Mouse(Animal):
    def get_legs_count(self):
        return DEFAULT_MOUSE_LEG_COUNT


class Snake(Animal):
    def get_legs_count(self):
        return DEFAULT_SNAKE_LEG_COUNT


animals = [
    Lion(),
    Mouse(),
    Snake()
]


animal_leg_count(animals)


"""
When it’s passed to the animal_leg_count function, it returns the number of legs
an animal has.

You see, the animal_leg_count doesn’t need to know the type of Animal to return
its leg count, it just calls the get_legs_count method of the Animal type because by
contract a sub-class of Animal class must implement the get_legs_count function.
"""
