# Adapter Design Pattern
## Overview 
The Bridge pattern is similar to the Adapter pattern except in the intent that you developed it.

The Bridge is an approach to refactor already existing code, whereas the Adapter creates an interface on top of existing code through existing available means without refactoring any existing code or interfaces.

The motivation for converting your code to the Bridge pattern is that it may be tightly coupled. There is logic and abstraction close together that is limiting your choices in how you can extend your solution in the way that you need.

E.g., you may have one Car class, that produces a very nice car. But you would like the option of varying the design a little, or outsourcing responsibility of creating the different components.

The Bridge pattern is a process about separating abstraction and implementation, so this will give you plenty of new ways of using your classes.
```
CAR = Car()
print(CAR)
> Car has wheels and engine and windows and everything else.
```
But you would like to delegate the engine dynamically from a separate set of classes or solutions.
```
ENGINE = EngineA()
CAR = Car(EngineA)
```
A Bridge didn't exist before, but since after the separation of interface and logic, each side can be extended independently of each other.

Also, the application of a Bridge in your code should use composition instead of inheritance. This means that you assign the relationship at runtime, rather than hard coded in the class definition.
I.e., CAR = Car(EngineA) rather than class Car(EngineA):

A Bridge implementation will generally be cleaner than an Adapter solution that was bolted on. Since it involved refactoring existing code, rather than layering on top of legacy or third-party solutions that may not have been intended for your particular use case.

You are the designer of the Bridge, but both approaches to the problem may work regardless.

The implementer part of a Bridge, can have one or more possible implementations for each refined abstraction. E.g., The implementor can print to paper, or screen, or format for a web browser. And the abstraction side could allow for many permutations of every shape that you can imagine.
## Decorator UML Diagram
<picture>
  <img alt="Decorator Parttern UML Diagram" src="./UML/bridge_concept.svg">
</picture>

## Builder Example UML Diagram
<picture> 
  <img alt="Decorator Parttern Example UML Diagram" src="./UML/bridge_example.svg">
</picture>

## Summary
- Use the decorator when you want to add responsibilities to objects dynamically without affecting the inner object.
- You want the option to later remove the decorator from an object in case you no longer need it.
- It is an alternative method to creating multiple combinations of subclasses. I.e., Instead of creating a subclass with all combinations of objects A, B, C in any order, and including/excluding objects, you could create 3 objects that can decorate each other in any order you want. E.g., (D(A(C))) or (B(C)) or (A(B(A(C))))
- The decorator, compared to using static inheritance to extend, is more flexible since you can easily add/remove the decorators at runtime. E.g., use in a recursive function.
- A decorator supports recursive composition. E.g., halve(halve(number))
- A decorator shouldn't modify the internal objects data or references. This allows the original object to stay intact if the decorator is later removed.