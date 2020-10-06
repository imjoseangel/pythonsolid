# Interface Segregation Principle

## Definition

Make fine grained interfaces that are client specific Clients should not be forced to depend upon interfaces or methods that they do not use. This principle deals with the disadvantages of implementing big interfaces.

## Description

Lets look at the first example in this section:

```python
class Animal:
    def get_legs_lion(self):
        raise NotImplementedError

    def get_legs_mouse(self):
        raise NotImplementedError

    def get_legs_snake(self):
        raise NotImplementedError
```

This interface counts legs for lions, mouses and snakes. class `Lion`, `Mouse` or `Snake` implementing the `Animal` interface must define the methods `get_legs_lion()`, `get_legs_mouse()`, `get_legs_snake()`.

```python
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
```

It’s quite funny looking at the code above. class `Lion` implements methods (`get_legs_mouse` and `get_legs_snake`) it has no use of, likewise `Mouse` implementing `get_legs_lion`, and `get_legs_snake`, and class `Snake` (`get_legs_lion`, `get_legs_mouse`).

If we add another method to the Animal interface, like `get_legs_girafe()`,

```python
class Animal:
    def get_legs_lion(self):
        raise NotImplementedError

    def get_legs_mouse(self):
        raise NotImplementedError

    def get_legs_snake(self):
        raise NotImplementedError

    def get_legs_girafe(self):
        raise NotImplementedError
```

The classes must implement the new method or error will be thrown.

We see that it is impossible to implement an animal that can count lion legs but not mouse or snake or girafe ones. We can just implement the methods to throw an error that shows the operation cannot be performed.

*Interface Segregation Principle* frowns against the design of this `Animal` interface. Clients (here `Lion`, `Mouse` and `Snake`) should not be forced to depend on methods that they do not need or use.  Also, *Interface Segregation Principle* states that interfaces should perform only one job (just like the *Single Responsability Principle*) any extra grouping of behavior should be abstracted away to another interface.

Here, our `Animal` interface performs actions that should be handled independently by other interfaces.

To make our `Animal` interface conform to the *Interface Segregation Principle*, we segregate the actions to different interfaces. Classes (`Lion`, `Mouse`, `Snake`, `Girafe`, etc) can just inherit from the `Animal` interface and implement their own `get_legs_count` behavior.

```python
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
```

We can then use the I-interfaces to create Animal specifics like Elephant, Zebra, Bull, Goat, etc.

## Clone Example Repository

Clone the example repository with the command `git clone https://github.com/imjoseangel/pythonsolid.git solid-examples`

## Run the Examples

Within the root of a repository, the examples are under a directory called `examples`.

### First example (Bad Design Pattern)

Open the *example01* file under the bad directory: [`solid-examples/examples/bad/04_interfacesegregation/example01.py`](examples/bad/04_interfacesegregation/example01.py)

You can run it with the command `clear && python solid-examples/examples/bad/04_interfacesegregation/example01.py`

From the `Snake` class remove the `get_legs_lion` method and keep only this:

```python
class Snake(Animal):

    def get_legs_mouse(self):
        print(DEFAULT_MOUSE_LEG_COUNT)

    def get_legs_snake(self):
        print(DEFAULT_SNAKE_LEG_COUNT)
```

Run it again:

`clear && python solid-examples/examples/bad/04_interfacesegregation/example01.py`

The following error is thrown:

```python
TypeError: Can't instantiate abstract class Snake with abstract methods get_legs_lion
```

### Second example (Good Design Pattern)

Open the *example01* file under the good directory: [`solid-examples/examples/good/04_interfacesegregation/example01.py`](examples/good/04_interfacesegregation/example01.py)

You can run it with the command `clear && python solid-examples/examples/good/04_interfacesegregation/example01.py`
