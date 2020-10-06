# Dependency Inversion Principle

## Definition

Dependency should be on abstractions not concretions A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions. B. Abstractions should not depend on details. Details should depend upon abstractions.

There comes a point in software development where our app will be largely composed of modules. When this happens, we have to clear things up by using dependency injection. High-level components depending on low-level components to function.

## Description

Lets look at the first example in this section:

```python
class Lion:
    pass

class Manager:
    def __init__(self):
        self.animal = None

    def set_animal(self, animal):
        assert isinstance(
            animal, Lion), "`animal` must be of type {}".format(Lion)

        self.animal = animal

    def get_legs_count(self):
        if self.animal is not None:
            self.animal.get_legs_count()
```

Here, `Manager` is the high-level component whereas `Lion` is the low-level component. This design violates *Dependency Inversion Principle* A: High-level modules should not depend on low-level level modules. It should depend upon its abstraction.

The `Manager` class is forced to depend upon the `Lion` class. If we need to change the `Manager` service, maybe we want to add animal sound, we will painstakingly have to move through all the instances of `Manager` to edit the code and this violates the *Open-Closed Principle*.

The Manager class should care less the type of animal you are using. We make an Animal interface:

```python
class Animal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_legs_count(self):
        pass
```

The Animal interface has a `get_legs_count` method. With this, we pass in an argument of type `Animal` to our `Manager` class:

```python
class Manager:
    def __init__(self):
        self.animal = None

    def set_animal(self, animal):
        assert isinstance(
            animal, Animal), "`animal` must be of type {}".format(Animal)

        self.animal = animal

    def get_legs_count(self):
        if self.animal is not None:
            self.animal.get_legs_count()
```

So now, no matter the type of `Animal` service passed to `Manager` it can easily get the animal properties without bothering to know the type of animal.

We can now re-implement our `Lion` class to implement the `Animal` interface:

```python
class Lion(Animal):

    def get_legs_count(self):
        print(DEFAULT_LION_LEG_COUNT)
```

We can create many `Animal` types and pass it to our `Manager` class without any fuss about errors:

```python
class Mouse(Animal):

    def get_legs_count(self):
        print(DEFAULT_MOUSE_LEG_COUNT)


class Snake(Animal):

    def get_legs_count(self):
        print(DEFAULT_SNAKE_LEG_COUNT)
```

Now, we can see that both high-level modules and low-level modules depend on abstractions. `Manager` class(high level module) depends on the `Animal` interface(abstraction) and the animal types(low level modules) in turn,
depends on the `Animal` interface(abstraction).

Also, this *Dependency Inversion Principle* will force us not to violate the *Liskov Substitution Principle*:
The animal types Lion-Mouse-Snake are substitutable for their parent type `Animal`.

## Clone Example Repository

Clone the example repository with the command `git clone https://github.com/imjoseangel/pythonsolid.git solid-examples`

## Run the Examples

Within the root of a repository, the examples are under a directory called `examples`.

### First example (Bad Design Pattern)

Open the *example01* file under the bad directory: [`solid-examples/examples/bad/05_dependencyinversion/example01.py`](examples/bad/05_dependencyinversion/example01.py)

You can run it with the command `clear && python3 solid-examples/examples/bad/05_dependencyinversion/example01.py`

### Second example (Good Design Pattern)

Open the *example01* file under the good directory: [`solid-examples/examples/good/05_dependencyinversion/example01.py`](examples/good/05_dependencyinversion/example01.py)

You can run it with the command `clear && python3 solid-examples/examples/good/05_dependencyinversion/example01.py`
