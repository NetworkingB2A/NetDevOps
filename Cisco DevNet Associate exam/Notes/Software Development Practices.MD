## Understanding Design patterns

You write this to show exactly what you are trying to accomplish. A design pattern is a map. This is not code. a set of rules on how you can write code.

take a look at the following book:
Design patterns: element of reusable object-oriented software
ISBN-13: 978:021633610

## Different design patterns
### Singleton Design pattern
![Singleton Design pattern](../../images/Singleton%20Design.png)

- A pattern that restricts classes to only being instantiated once during the execution of a program.
  - Examples include - Data base connections, configuration values, static values, ect
- A class with a private instance variable representing it's only instance, a public get instance() method to retrieve that object, a constructor to enforce a single-instantiation.
- Extra steps are needed to make a singleton design work. other languages like java and c# will work automatically.
- Example code view Sample code/singleton.py

### Observer Pattern
![Observer Design pattern](../../images/Observer%20Pattern.png)
A pattern where dependent objects are updated or modified by one or more subject objects
- Allows objects to react or respond in response to events.
- Popular in UI systems

Two classes defined by observer pattern:
- Subject - Which maintains a list of observers and includes methods for attaching, detaching, and notifying observers.
- Observer - Which has a method to receive updates from subjects.
- Example code view Sample code/observer.py

### Model, View, Controller (MVC)
A high-level abstraction where responsibilities are divided up into three loosely coupled components.
- Model: The component that stores the data
- View: The component that displays data
- Controller: The component that handles logic flow, user interaction, and directs models and views.