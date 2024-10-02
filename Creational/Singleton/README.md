# Singleton Design Pattern
## Overview 
Sometimes you need an object in an application where there is only one instance.

You don't want there to be many versions, for example, you have a game with a score, and you want to adjust it. You may have accidentally created several instances of the class holding the score object. Or, you may be opening a database connection, there is no need to create many, when you can use the existing one that is already in memory. You may want a logging component, and you want to ensure all classes use the same instance. So, every class could declare their own logger component, but behind the scenes, they all point to the same memory address (ID).

By creating a class and following the Singleton pattern, you can enforce that even if any number of instances were created, they will still refer to the original class.

The Singleton can be accessible globally, but it is not a global variable. It is a class that can be instanced at any time, but after it is first instanced, any new instances will point to the same instance as the first.

For a class to behave as a Singleton, it should not contain any references to self but use static variables, static methods and/or class methods.
## Singleton UML Diagram
<picture>
  <img alt="Singleton Parttern UML Diagram" src="./UML/singleton_concept.svg">
</picture>

## Builder Example UML Diagram
<picture> 
  <img alt="Singleton Parttern Example UML Diagram" src="./UML/singleton_example.svg">
</picture>

## Summary
To be a Singleton, there must only be one copy of the Singleton, no matter how many times, or in which class it was instantiated.
You want the attributes or methods to be globally accessible across your application, so that other classes may be able to use the Singleton.
You can use Singletons in other classes, as I did with the leaderboard, and they will all use the same Singleton regardless.
You want controlled access to a sole instance.
For a class to act as a singleton, it should not contain any references to self.