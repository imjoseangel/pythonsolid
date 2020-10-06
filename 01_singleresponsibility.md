# Single Responsibility Principle

## Definition

A class or module should have one, and only one, reason to change. If a class has more than one responsibility, it becomes coupled. A change to one responsibility results to modification of the other responsibility.

## Description

Lets look at the first example in this section:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'

    def save(self, animal):
        pass

animal = Animal('Lion')
animal.save(animal)
```

The Animal class violates the *Single Responsibility Principle*.

### How does it violate Single Responsibility Principle

*Single Responsibility Principle* states that classes should have one responsibility, here, we can draw out two responsibilities: animal database management and animal properties management. The constructor and `get_name` manage the `Animal` properties while the `save` manages the `Animal` storage on a database.

### How will this design cause issues in the future

If the application changes in a way that it affects database management functions. The classes that make use of `Animal` properties will have to be touched and recompiled to compensate for the new changes.

You see this system smells of rigidity, it’s like a domino effect, touch one card it affects all other cards in line.

To make this conform to *Single Responsibility Principle*, we create another class that will handle the sole responsibility of storing an animal to a database:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'

class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

animal = Animal('Lion')
db = AnimalDB()
db.save(animal)
```

> When designing our classes, we should aim to put related features together, so whenever they tend to change they change for the same reason.  And we should try to separate features if they will change for different reasons. - **Steve Fenton**

The downside of this solution is that the clients of the this code have to deal with two classes.  A common solution to this dilemma is to apply the *Facade pattern*. The `Animal` class will be the Facade for the animal database management and the animal properties management.

```python
class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self) -> str:
        return f'My name is: {self.name}'

    def get(self, id):
        return self.db.get_animal(id)

    def save(self):
        self.db.save(animal=self)

class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

animal = Animal('Lion')
animal.save()
```

The most important methods are kept in the `Animal` class and used as Facade for the lesser functions.

## Clone Example Repository

Clone the example repository with the command `git clone https://github.com/imjoseangel/pythonsolid.git solid-examples`

## Run the Examples

Within the root of a repository, the examples are under a directory called `examples`.

### First example (Bad Design Pattern)

Open the *example01* file under the bad directory: ![solid-examples/examples/bad/01_singleresponsibility/example01.py](RHCE.jpg)`examples/bad/01_singleresponsibility/example01.py`

You can run it with the command `clear && python3 solid-examples/examples/bad/01_singleresponsibility/example01.py`{{execute}}

### Second example (Good Design Pattern)

Open the *example01* file under the good directory: `solid-examples/examples/good/01_singleresponsibility/example01.py`{{open}}

You can run it with the command `clear && python3 solid-examples/examples/good/01_singleresponsibility/example01.py`{{execute}}

### Third example (Good Design Pattern with Facade)

Open the *example02* file under the good directory: `solid-examples/examples/good/01_singleresponsibility/example02.py`{{open}}

You can run it with the command `clear && python3 solid-examples/examples/good/01_singleresponsibility/example02.py`{{execute}}
