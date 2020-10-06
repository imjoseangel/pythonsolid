# Open-Closed Principle

## Definition

Software entities(Classes, modules, functions) should be open for extension but closed for modification.

## Description

Lets look at the first example in this section:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'Lion':
            print('Roar!!!')
        elif animal.name == 'Mouse':
            print('Squeak!!!')

animals = [
    Animal('Lion'),
    Animal('Mouse')
]

animal_sound(animals)
```

The function `animal_sound` does not conform to the *Open-Closed Principle* because it cannot be closed against new kinds of animals. If we add a new animal, Snake, we have to modify the `animal_sound` function. You see, for every new animal, a new logic is added to the `animal_sound` function. This is quite a simple example. When your application grows and becomes complex, you will see that the if statement would be repeated over and over again in the `animal_sound` function each time a new animal is added, all over the application:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'Lion':
            print('Roar!!!')
        elif animal.name == 'Mouse':
            print('Squeak!!!')
        elif animal.name == 'Snake':
            print('Sssss!!!')

animals = [
    Animal('Lion'),
    Animal('Mouse'),
    Animal('Snake')
]

animal_sound(animals)
```

### How do we make the `animal_sound` function conform to *Open-Closed Principle*

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'

    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'Roar!!!'


class Mouse(Animal):
    def make_sound(self):
        return 'Squeak!!!'

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animals = [
    Lion('Lion'),
    Mouse('Mouse')
]

animal_sound(animals)
```

If we want to add new animal, then we can extend from `Animal` class. That's why it's correct according to the *Open-Closed Principle*:

```python
class Snake(Animal):
    def make_sound(self):
        return 'Sssss!!!'
```

`Animal` now has a virtual method `make_sound`. We have each animal extend the `Animal` class and implement the virtual `make_sound` method.

Every animal adds its own implementation on how it makes a sound in the `make_sound`. The `animal_sound` iterates through the array of animal and just calls its `make_sound` method.

Now, if we add a new animal, `animal_sound` doesn’t need to change. All we need to do is add the new animal to the animal array.

`animal_sound` now conforms to the *Open-Closed Principle*.

## Another example

Let’s imagine you have a store, and you give a discount of 20% to your favorite customers using this class: When you decide to offer double the 20% discount to VIP customers. You may modify the class like this:

```python
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
```

This example does not follows the *Open-Closed Principle*. If we want to give a new percent discount to a different customer type, you will need to add a new logic to the `Discount` class.

To make it follow the *Open-Closed Principle*, we will add a new class that will extend the `Discount`. In this new class, we would implement its new behavior:

```python
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2

class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
```

If you decide 80% discount to super VIP customers, it should be like: Extension without modification.

```python
class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2

customer, price = 'Jan', 100

assert Discount(customer, price).get_discount() == 20.0
assert VIPDiscount(customer, price).get_discount() == 40.0
assert SuperVIPDiscount(customer, price).get_discount() == 80.0
```

## Clone Example Repository

Clone the example repository with the command `git clone https://github.com/imjoseangel/pythonsolid.git solid-examples`

## Run the Examples

Within the root of a repository, the examples are under a directory called `examples`.

### First example (Bad Design Pattern)

Open the *example01* file under the bad directory: [`solid-examples/examples/bad/02_openclosed/example01.py`](examples/bad/02_openclosed/example01.py)

You can run it with the command `clear && python3 solid-examples/examples/bad/02_openclosed/example01.py`

#### Add new item to First example

Open the *example02* file under the bad directory: [`solid-examples/examples/bad/02_openclosed/example02.py`](examples/bad/02_openclosed/example02.py)

You can run it with the command `clear && python3 solid-examples/examples/bad/02_openclosed/example02.py`

### Second example (Good Design Pattern)

Open the *example01* file under the good directory: [`solid-examples/examples/good/02_openclosed/example01.py`](examples/good/02_openclosed/example01.py)

You can run it with the command `clear && python3 solid-examples/examples/good/02_openclosed/example01.py`

#### Add new item to Second example

Open the *example02* file under the good directory: [`solid-examples/examples/good/02_openclosed/example02.py`](examples/good/02_openclosed/example02.py)

You can run it with the command `clear && python3 solid-examples/examples/good/02_openclosed/example02.py`

### Third example (Bad Design Pattern)

Open the *example03* file under the bad directory: [`solid-examples/examples/bad/02_openclosed/example03.py`](examples/bad/02_openclosed/example03.py)

You can run it with the command `clear && python3 solid-examples/examples/bad/02_openclosed/example03.py`

### Fourth example (Good Design Pattern)

Open the *example03* file under the good directory: [`solid-examples/examples/good/02_openclosed/example03.py`](examples/good/02_openclosed/example03.py)

You can run it with the command `clear && python3 solid-examples/examples/good/02_openclosed/example03.py`
