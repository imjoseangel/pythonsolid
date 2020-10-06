"""
Interface Segregation Principle

Make fine grained interfaces that are client specific Clients should not be
forced to depend upon interfaces or methods that they do not use. This principle
deals with the disadvantages of implementing big interfaces.

Let’s look at the below Animal interface:
"""


class Animal:
    def get_legs_lion(self):
        raise NotImplementedError

    def get_legs_mouse(self):
        raise NotImplementedError

    def get_legs_snake(self):
        raise NotImplementedError


"""
This interface counts legs for lions, mouses and snakes. class Lion, Mouse or
Snake implementing the Animal interface must define the methods get_legs_lion(),
get_legs_mouse(), get_legs_snake().
"""


class Lion(Animal):
    def get_legs_lion(self):
        pass

    def get_legs_mouse(self):
        pass

    def get_legs_snake(self):
        pass


class Mouse(Animal):
    def get_legs_lion(self):
        pass

    def get_legs_mouse(self):
        pass

    def get_legs_snake(self):
        pass


class Snake(Animal):
    def get_legs_lion(self):
        pass

    def get_legs_mouse(self):
        pass

    def get_legs_snake(self):
        pass


"""
It’s quite funny looking at the code above. class Lion implements methods
(get_legs_mouse and get_legs_snake) it has no use of, likewise Mouse implementing
get_legs_lion, and get_legs_snake, and class Snake (get_legs_lion, get_legs_mouse).

If we add another method to the Animal interface, like get_legs_girafe(),
"""


class Animal:
    def get_legs_lion(self):
        raise NotImplementedError

    def get_legs_mouse(self):
        raise NotImplementedError

    def get_legs_snake(self):
        raise NotImplementedError

    def get_legs_girafe(self):
        raise NotImplementedError


"""
The classes must implement the new method or error will be thrown.

We see that it is impossible to implement an animal that can count lion legs but not
mouse or snake or girafe ones. We can just implement the methods to throw an error
that shows the operation cannot be performed.

Interface Segregation Principle frowns against the design of this Animal interface.
Clients (here Lion, Mouse and Snake) should not be forced to depend on methods
that they do not need or use.  Also, Interface Segregation Principle states that interfaces
should perform only one job (just like the Single Responsability Principle) any extra
grouping of behavior should be abstracted away to another interface.

Here, our Animal interface performs actions that should be handled independently
by other interfaces.

To make our Animal interface conform to the Interface Segregation Principle, we
segregate the actions to different interfaces. Classes (Lion, Mouse, Snake, Girafe,
etc) can just inherit from the Animal interface and implement their own get_legs_count
behavior.
"""


class Animal:
    def get_legs_count(self):
        raise NotImplementedError


class Lion(Animal):
    def get_legs_count(self):
        pass


class Mouse(Animal):
    def get_legs_count(self):
        pass


class Snake(Animal):
    def get_legs_count(self):
        pass


"""
We can then use the I-interfaces to create Animal specifics like Elephant,
Zebra, Bull, Goat, etc.
"""
