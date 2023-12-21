pyATS has a learn hostname feature
- https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/connection.html?highlight=learn_hostname#customizing-your-connection

List of apis for pyATS
- https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/services/index.html


Pyats testing

Nautobot/netbox as your source of truth, meaning that this has your config, This has your connections. you run a pre-change device test and find the current state of your device/network

Pyats as configuration engine?


you would want to create a suite of tests based on what task you are performing.
This is my Device device os upgrade testing suite
This is my vlan change testing suite
This is my routing change testing suite.
This is my HR change testing suite.
ECT.


Golden config checks. HR switches should have this NTP server, other switches should have this other NTP server.


Connections Manager: A connection represents communication with the target device for management and monitoring. All connections to the same target device are managed through a dedicated, high-level manager that provides resource allocation, control and conflict management, and, finally, seamless integration to device object instances in a topology.

Configuration Manager: A Python object (devices and configurable characteristics) is where you set some attributes, and the configuration generates automatically. CLI configuration is possible and easy, but with the pyATS Library (Genie), you configure a network device by following a common structure that works across multiple platforms. Each object follows a structure that is based on a feature or set of features.

Parsers: A parser converts device output into a Python dictionary that stores the device data as a set of key-value pairs. The pyATS Library parsers create standardized output for commands, meaning you can write and run reusable automation scripts. The purpose of parsing is to put all the output generated from any command in a device operating system into a single data structure.

Network profiling: The pyATS Library Ops module provides a representation of the current operational state of a device, per feature (protocol). It “learns” the operational state by executing a series of commands and parsing the output into a common data structure across various operating systems. The purpose of network profiling is to get and save (a snapshot) from any moment in the operational state of the network.

Network states comparison: Once the network is profiled and snapshots are available, those snapshots can be compared and differences can be discovered, analyzed, and processed.

AEest: Automation Easy Testing (AETest) is the standard test engineering automation harness. It offers a simple and straightforward way for users to define, execute, and debug testcases and testscripts.


There are two different ways to run pyats scripts.
one is command line in linux. the other is running a jobs file.

- CommonSetup
  - subsectiona
  - subsectionb
- Testcase 1
  - aetest.setup
  - aetest.test
- Testcase 2
  - aetest.test
  - aetest.test
- CommonCleanup
  - subsectiona
  - subsectionb

Here is an example of a testbed object and how it all works together.
The interesting note here is that everything is some sort of an object.

```
+--------------------------------------------------------------------------+
| Testbed Object                                                           |
|                                                                          |
| +-----------------------------+          +-----------------------------+ |
| | Device Object - myRouterA   |          | Device Object - myRouterB   | |
| |                             |          |                             | |
| |         device interfaces   |          |          device interfaces  | |
| | +----------+ +----------+   |          |   +----------+ +----------+ | |
| | | intf Obj | | intf Obj |   |          |   |  intf Obj| | intf Obj | | |
| | | Eth1/1   | | Eth1/2 *-----------*----------*  Eth1/1| | Eth1/2   | | |
| | +----------+ + ---------+   |     |    |   +----------+ +----------+ | |
| +-----------------------------+     |    +-----------------------------+ |
|                                     |                                    |
|                               +-----*----+                               |
|                               | Link Obj |                               |
|                               |rtrA-rtrB |                               |
|                               +----------+                               |
+--------------------------------------------------------------------------+
```

For the Yaml file (if you use a yaml file), you would have a testbed block. The testbed block is the defaults that all your devices will use. Example would be username and passwords.
Then the device object would house info about the device and how to connect to the devices.
To me Netbox plays an important role, in the fact that  I should be able to create a device object, interface object, link object all from the netbox data.




THINGS TO LOOK UP LATER

unicon.Unicon – example was used in the testbed for connections to a device.

Try except else



First testcase I would like to write is 
"Is bin file on device?"
"does the hash of the bin file and the cisco created hash match?"


pyATS has a learn hostname feature
- https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/connection.html?highlight=learn_hostname#customizing-your-connection

List of apis for pyATS
- https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/services/index.html


Pyats testing

Nautobot/netbox as your source of truth, meaning that this has your config, This has your connections. you run a pre-change device test and find the current state of your device/network

Pyats as configuration engine?


you would want to create a suite of tests based on what task you are performing.
This is my Device device os upgrade testing suite
This is my vlan change testing suite
This is my routing change testing suite.
This is my HR change testing suite.
ECT.


Golden config checks. HR switches should have this NTP server, other switches should have this other NTP server.


Connections Manager: A connection represents communication with the target device for management and monitoring. All connections to the same target device are managed through a dedicated, high-level manager that provides resource allocation, control and conflict management, and, finally, seamless integration to device object instances in a topology.

Configuration Manager: A Python object (devices and configurable characteristics) is where you set some attributes, and the configuration generates automatically. CLI configuration is possible and easy, but with the pyATS Library (Genie), you configure a network device by following a common structure that works across multiple platforms. Each object follows a structure that is based on a feature or set of features.

Parsers: A parser converts device output into a Python dictionary that stores the device data as a set of key-value pairs. The pyATS Library parsers create standardized output for commands, meaning you can write and run reusable automation scripts. The purpose of parsing is to put all the output generated from any command in a device operating system into a single data structure.

Network profiling: The pyATS Library Ops module provides a representation of the current operational state of a device, per feature (protocol). It “learns” the operational state by executing a series of commands and parsing the output into a common data structure across various operating systems. The purpose of network profiling is to get and save (a snapshot) from any moment in the operational state of the network.

Network states comparison: Once the network is profiled and snapshots are available, those snapshots can be compared and differences can be discovered, analyzed, and processed.

AEest: Automation Easy Testing (AETest) is the standard test engineering automation harness. It offers a simple and straightforward way for users to define, execute, and debug testcases and testscripts.


### Each Test script has three major container sections:
- #### CommonSetup
  - This is the actions that are common to all the devices you are testing. This is an optional part of testscript. It includes teh following tasks:
    - Check the validity of script inputs.
    - Connect to all testbed devices and check that they are ready, with all the required images, features, hardware and licenses.
    - Configure and bring up the device interface and topology.
    - Confirm that all devices are reachable.
    - Set up and load the base configuration that is common or shared between all testcases.
- #### Testcases
  - This section collects all of your smaller tests. Each test case may have an arbitrary number of smaller test sections:
    - Each testcase can have its own setup and cleanup section for any small changes that must be removed before the next testcase.
    - Tests inside a testcase run in the order that you define.
    - Testcase include at least one testcase, and it is a mandatory part of your testscript.
- #### Common Cleanup
  - CommonCleanup is the last section to run within each testscript. Any config, initializations and environment changes that occurred during the script run should be cleaned up or removed here. Clean up here includes:
    - Removing any lingering changes that remain from previous testcases.
    - Return all devices to their initial state.
    - Disconnect from devices in your testbed.
    - Remove any unnecessary configuration from test devices.
    - Reset a device.

A testcase should contain three sections:
- Setup section
- Test sections
  - smallest unit of testing and the most basic building block.
  - Each test should carry out a single identifiable check or evaluation to be completed as part of the greater section.
  - A test section group actions (triggers) and validations (verifications).
  - A testcase consists of at least one mandatory test section.
- Cleanup sections



NOTES
- You can set up a configuration file that would email out the results. This could be cool when the devices are updating. I wonder if you could create a page out if a device doesnt come up like you expect.
- 