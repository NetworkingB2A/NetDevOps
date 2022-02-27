Model-Driven Programmability

gRPC is an open-source project started by Google to provide a modern remote procedure call framework that can be used in any environment.

## NETCONF
NETCONF = Network Configuration Protocol
NETCONF is just the connection and configuration protocol to a network device. If you need to send acutaul data, this is where YANG (Yet another next generation) steps in. With YANG you have a way to format your device data that you can push to your end devices.  
NETCONF uses SSH as its communication layer. It uses a client server model.  
Messages send with NETCONG use RPCs.

### NETCONF Operations
| Operation | Description | 
|-|-| 
\<get> | Retrieve running configurations and device state information.
\<get-config> | Retrieve all or part of the specified configuration data store.
\<edit-config> | Load all or part of a configuration to specified configuration data store.
\<copy-config> | Replace an entire configuration data store.
\<delete-config> | Delete a configuration data store.
\<commit> | Copy the candidate data store to the running data store.
\<lock>/\<unlock> | Lock or unlock the entire configuration data store system.
\<close-session> | Gracefully terminate the NETCONF session.
\<kill-session> | Forcibly terminate teh NETCONF session.

The NETCONF \<edit-config> operations supports several attributes
- merge
- replace
- create
- delete