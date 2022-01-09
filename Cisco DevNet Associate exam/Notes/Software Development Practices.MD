# Software development lifecycle
### What is SDLC (Software development lifecycle)?
SDLC is a generic process. The following is the overall stages
- Stage 1 - Planning
  - Can also be called requirement analysis. Identify the problem, get input from stakeholders.
- Stage 2 - Defining
  - What should your program do at the end?  
- Stage 3 - Designing  
  - You turn software specifications into a design specification. Users must have buy in at this stage
- Stage 4 - Building  
  - This is where you start to work on the code.
- Stage 5 - Testing  
  - Test code for bugs or defects.
- Stage 6 - Deployment  
  - This is where you put your software into production.

## Software Development methods
### Waterfall
Waterfall is the older way of designing code. This method follows the SDLC down to a T. The problem is that you do not deliver a product until it is completed. You may spend years writing the code before ever pushing the code into production. if you are halfway done writting the code, you still have delivered 0 product.  
Waterfall does not handle changes well at all. If need to make a change during the coding phase, that might mean you need to take a step backwards and move back into planning.  
Three major challanges for waterfall include
- The serial nature of waterfall
- Value is not achieved until the end
- Quality can often suffer

### Lean
Three main goals for the lean method
- Elimination of waste
  - if something doesn't add value to the final product. Get rid of it
- Just-in-time
  - Don't build something until the customer is ready to buy it.
- Continues improvement
  - Always improve your processes with lessons learned.

### Agile
One key factor of agile, is breaking your work into short sprint(2 weeks is typical). At the end of every sprint, you should have something to deliver to your program.  
You would first create the bare minimum viable product. This may not deliver every part of your whole product, but you just delivered a product to your users that can start to be used right away. At the end of the next sprint you will have another feature, and the next sprint you will have another feature. You will continue to deliver products over and over again, while finding bugs along the way. You may also find out that one of the original goals will need to be scraped. This is no longer a big deal because you may have not spent time writing this code and you just ended up saving yourself a bunch of time.

The Agile Manifesto
- Customer satisfaction is provided through early and continuous delivery of valuable software.
- Changing requirements, even in late development, are welcome.
- Working software is delivered frequently (in weeks rather than months).
- The process depends on close, daily cooperation between business stakeholders and developers.
- Projects are built around motivated individuals, who should be trusted.
- Face-to-face conversation is the best form of communication (co-location).
- Working software is the principal measure of progress.
- Sustainable development requires being able to maintain a constant pace.
- Continuous attention is paid to technical excellence and good design.
- Simplicity—the art of maximizing the amount of work not done—is essential.
- The best architectures, requirements, and designs emerge from self-organizing teams.
- A team regularly reflects on how to become more effective and adjusts accordingly.

# Design Patterns
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
- The observer pattern is often used to handle communication between the model and the view in the MVC pattern.

Two classes defined by observer pattern:
- Subject - Which maintains a list of observers and includes methods for attaching, detaching, and notifying observers.
- Observer - Which has a method to receive updates from subjects.
- Example code view Sample code/observer.py

### Model, View, Controller (MVC)
A high-level abstraction where responsibilities are divided up into three loosely coupled components. This design type is often used in web development.
- Model: The component that retrieves and manipulates the data. Often tied to a database.
- View: The component that displays data. It's what the end users see on their devices. 
- Controller: The component that handles logic flow, user interaction, and directs models and views.

Conducting code reviews