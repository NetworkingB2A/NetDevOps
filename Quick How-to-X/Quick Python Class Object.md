

# Here is a very simple class
This class has a doc string created. I created a hidden method, a normal method, and a overloaded method.

The hidden method is `_verify_required_attributes_set()` and is to check to make sure the user passed all of the attributes.
The normal method is `print_ip_address()` and is to let a user quickly print out a ip address.
The overloaded methods are `__init__()` and `__repr__()`. `__init__()` is used to instantiate the object. `__repr__()` is used to allow the user to print friendly looking data to the screen.


``` python

class NetworkDevice:

    """
    A class to create a simple network device object.
    
    ...
    
    Attributes
    ----------
    hostname : str (Required)
        Name of the network device
    host_ip_address : str (Required)
        IP address of the host device
    host_username : str (Required)
        Username used to authenticate to network device
    host_password : str (Required)
        Password used to authenticate to network device
        
    Methods
    -------
    
    print_ip_address():
        Prints out network devices IP address.
    
    
    
    """
    def __init__(self, hostname=None, host_ip_address=None, host_username=None, host_password=None ):
        self.hostname = hostname
        self.host_ip_address = host_ip_address
        self.host_username = host_username
        self.host_password = host_password
        self._verify_required_attributes_set()

    def _verify_required_attributes_set(self):
        """
        I want this method just to make sure a user passed in all required attributes. 
        Raises an error if any were missed. I could make this a lot more robust by checking against specific objects. I won't go into details here.
        """
        if self.hostname is None:
            raise AttributeError("hostname was not defined")
        if self.host_ip_address is None:
            raise AttributeError("host_ip_address was not defined")
        if self.host_username is None:
            raise AttributeError("host_username was not defined")
        if self.host_password is None:
            raise AttributeError("host_password was not defined")

    def print_ip_address(self):
        """ Method to print IP address."""
        print(f'\nThe host ip address is: {self.host_ip_address}\n')

    def __repr__(self):
        """
        This is called overloading a method, and this __repr__ is a specific python method.
        In this case I have used it to allow a user to do a print on an NetworkDevice object and give them something more easier to read.
        """
        return f'''
NetworkDevice: 
    Hostname: {self.hostname}
    Host IP Address: {self.host_ip_address}
    Host Username: {self.host_username}
    Host Password: {self.host_password}
'''

```

# Here is an example of how I would use this code

```python
>>> new_network_device = NetworkDevice(hostname="router1", host_ip_address="10.1.1.1", host_username="ciscoUsername", host_password="UsersPassword")
>>> print(new_network_device)

NetworkDevice: 
    Hostname: router1
    Host IP Address: 10.1.1.1
    Host Username: ciscoUsername
    Host Password: UsersPassword

>>> new_network_device.print_ip_address()

The host ip address is: 10.1.1.1

>>> NetworkDevice.__doc__
'\n    A class to create a simple network device object.\n    \n    ...\n    \n    Attributes\n    ----------\n    hostname : str (Required)\n        Name of the network device\n    host_ip_address : str (Required)\n        IP address of the host device\n    host_username : str (Required)\n        Username used to authenticate to network device\n    host_password : str (Required)\n        Password used to authenticate to network device\n        \n    Methods\n    -------\n    \n    print_ip_address():\n        Prints out network devices IP address.\n    \n    \n    \n    '
>>> help(NetworkDevice)
Help on class NetworkDevice in module __main__:

class NetworkDevice(builtins.object)
 |  NetworkDevice(hostname=None, host_ip_address=None, host_username=None, host_password=None)
 |  
 |  A class to create a simple network device object.
 |  
 |  ...
 |  
 |  Attributes
 |  ----------
 |  hostname : str (Required)
 OMITTED REST FOR BREVITY
```