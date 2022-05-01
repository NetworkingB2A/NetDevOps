
## Cloud  

NIST defines cloud as three main category with additional subcategories. They are:
- Essential characteristics
  - Broad network access
  - Rapid elasticity
  - Measured service
  - On-demand self-service
  - Resource Pooling
- Service models
  - SaaS
  - PaaS
  - IaaS
- Deployment models
  - Public
  - Private
  - Hybrid
  - Community

Some benefits of containers include:
- Consistency for deployment automation
- Simplified lightweight image files measured in MB rather then GB
- Providing only what the app needs and nothing else
- Ability to work the same production as in a developer's laptop
- Ability to deploy applications in seconds

Notes about serverless:
- Of course there is still a server. but you dont need to work about the server at all.
- This is the idea that you write code, upload the code to a server and the server just runs the code.
- Works well if you just need a bit of code to run periodically.
- Can also be called function as a service.
- Advantages of serverless deployment
  - Cost
  - Scalability
  - Easier to use and write code for
- Disadvantages of serverless deployment
  - Latency to spin up the service when needed
  - Resource constraints
  - Monitoring and debugging
  - Security and privacy
  - Vendor lock-in

## DevOps

DevOps has five guiding principles
- Culture
  - For DevOps to work, organizational culture must change. 
  - This is the most important and more difficult part of DevOps
- Automation
- Lean
  - Reducing wasted efforts and streamlining the process.
- Measurement
  - If you never measure your results, you will never know what to improve or if you are improving.
- Sharing
  - Feedback and sharing is key to reach the ultimate goal.

### Putting devops into practice. The Three ways
First way: Systems and flow  
The following are key characteristics of the first way
- Make work visible
- Reduce batch sizes
- Reduce intervals of work
- Build in quality by preventing defects from being passed downstream 

Second way: Feedback loop
The following are key characteristics of the second way
- Amplify feedback to prevent problems from happening again
- Enable faster detection and recovery
- See problems as they occur and swarm them until they are fixed
- Maximize opportunities to learn and improve

Third way: Continuous Experimentation and Learning
The following are key characteristics of the third way
- Conduct dynamic, disciplined experimentation and risk taking
- Define time to fix issues and make the system better
- When things go wrong, don't point fingers
- Create shared code repositories

### DevOps Implementation
The stages for implementing DevOps generally follows these steps:
- Continuous integrations
  - This part involves merging dev code with production code and introduces automated testing.
- Continuous delivery
  - This stage involves a software package delivery mechanism for releasing code to staging for review and inspection.
- Continuous deployment
  - This stage relies on continuous integration and continuous delivery to automatically replace code into production as soon as it is ready.

