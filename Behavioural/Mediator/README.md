# Iterator Design Pattern
## Overview 
Objects communicate through the Mediator rather than directly with each other.

As a system evolves and becomes larger and supports more complex functionality and business rules, the problem of communicating between these components becomes more complicated to understand and manage. It may be beneficial to refactor your system to centralize some or all of its functionality via some kind of mediation process.

The mediator pattern is similar to implementing a Facade pattern between your objects and processes. Except that the structure of the Mediator allows multi-directional communication between the objects or processes that would normally be interacting directly with each other.

While the Facade is a structural pattern, and the Mediator also implies structure in the way that it exists between two or more other objects or processes, it also allows changing the behavior of the interaction to make it more cooperative in some way. E.g., the centralization of application logic, managing the routing behavior, caching, logging, etc.

## Iterator UML Diagram
![alt text](image.png)

## Builder Example UML Diagram
![alt text](image-1.png)

## Summary
- A mediator replaces a structure with many-to-many interactions between its classes and processes, with a one-to-many centralized structure where the interface supports all the methods of the many-to-many structure, but via the mediator component instead.
- The mediator pattern encourages usage of shared objects that can now be centrally managed and synchronized.
- The mediator pattern creates an abstraction between two or more components that then makes a system easier to understand and manage.
The mediator pattern is similar to the Facade pattern, except the Mediator is expected to transact data both ways between two or more other classes or processes that would normally interact directly with each other.