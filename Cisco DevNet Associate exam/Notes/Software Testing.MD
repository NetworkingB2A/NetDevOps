# Software Testing

## Software Test Types
The testing pyramid and a structured way of testing your code.
1. Tests from the upper layers are started when tests from the lower layers are finished.
2. There should be more tests executed in the lower layers than in the upper layers.

The most common layers are (from lowest layers to the highest)
1. Unit testing
   -  Unit testing should focus on internal system components. Testing methods, functions, procedure or even an entire class.
   -  Good unit tests should be reliable, isolated, fast and readable.
   -  One recommended practice for writing unit tests is to follow the "Arrange, Act Assert" principle.
      -  Arrange: Initialize variables and objects that are required for the test.
      -  Act: Run unit test
      -  Assert: Check if result matches what was expected.
2. Integration testing
   - When conducting integration testing, you can use one of the two approaches:
     - Big bang approach: requires all components to be finished and all the tests to use only actual components.
     - incremental approach: The component can be tested with it is developed. This approach requires test doubles to replace some dependencies. 
3. System testing
   - The list of types of systems tests that can be conducted includes:
     - Functionality testing
     - Installation testing
     - Usability testing
     - Security testing
     - Performance testing
     - Load testing
     - Stress testing
     - Configuration testing
     - Compatibility testing
     - Recovery testing
     - Procedure testing
4. Acceptance testing
   - This is the phase of testing where you have actual users testing out the software and get their feedback.
   - Examples include
     - Alpha testing
     - Beta testing
     - Contract testing
     - Regulation testing
     - Operational testing

### Unit Tests
Usually a unit is a single function, method, class or any statement inside these constructs that needs verification.

Unit testing frameworks
These concepts can be defined with the following terminology:
- Test fixture: Create a common state of the environment that is needed by the tests and return to the original state afterwards.
- Test case: The elemental component of a test; an individual unit of testing. It is used for checking for a specific response on a set of inputs.
- Test suite: An aggregation of test cases and other test suites that should be executed together using the same fixture. The order of the tests inside does not matter.
- Test runner: A component for orchestrating the execution of tests and providing a graphical of textual output of the testing results.