from pprint import pprint


class NetworkDevice:
    def __init__(self, model, manufacturer, **kwargs):
        self.model = model
        self.manufacturer = manufacturer
        self.kwargs = kwargs

    def __str__(self):
        """Represents this object as a string for pretty-printing"""
        return f"""
Object name: {self.__class__.__name__}
  model: {self.model}
  manufacturer: {self.manufacturer}
"""

    def __repr__(self):
        """Represents this object as a string for use in the REPL"""
        return f"<{self.__class__.__name__} (model={self.model}, manufacturer={self.manufacturer})>"

    def __eq__(self, other):
        """Used to determine if two objects of this class are equal to each other"""
        return bool(other.model == self.model) and bool(
            other.manufacturer == self.manufacturer
        )

    def __hash__(self):
        """Used to calculate a unique hash for this object, in case we ever want to use it in a dictionary or a set"""
        return hash((self.model, self.manufacturer))

    def boot_up(self):
        print("Network Device is now booting up")

    def __boot_up(self):
        # This will invoke name mangling. This will change the method name from __boot_up to _NetworkDevice__boot_up
        print("Network Device is now __booting up")


class NetworkRouter(NetworkDevice):
    def __init__(self, model, manufacturer, routed_interface_port):
        super().__init__(model, manufacturer)
        self.routed_interface_port = routed_interface_port

    def __str__(self):
        """Represents this object as a string for pretty-printing"""
        return f"""
Object name: {self.__class__.__name__} 
  model: {self.model}
  manufacturer: {self.manufacturer}
  router type: {self.routed_interface_port}
    """

    def __repr__(self):
        """Represents this object as a string for use in the REPL"""
        return f"<{self.__class__.__name__} (model={self.model}, manufacturer={self.manufacturer}, routed_interface_port={self.routed_interface_port})>"

    def __eq__(self, other):
        """Used to determine if two objects of this class are equal to each other"""
        return bool(hash(other) == hash(self))

    def __hash__(self):
        """Used to calculate a unique hash for this object, in case we ever want to use it in a dictionary or a set"""
        return hash((self.model, self.manufacturer, self.routed_interface_port))

    def boot_up(self):
        print("Network Router is now booting up")


class SDWanRouter(NetworkRouter):
    pass


class CoreRouter(NetworkRouter):
    def __init__(
        self, model, manufacturer, routed_interface_port, internal_routing_protocol
    ):
        super().__init__(model, manufacturer, routed_interface_port)
        self.internal_routing_protocol = internal_routing_protocol

    def print_routing_protocol(self):
        print(self.internal_routing_protocol)


class BoarderRouter(NetworkRouter):
    def __init__(
        self, model, manufacturer, routed_interface_port, external_routing_protocol
    ):
        super().__init__(model, manufacturer, routed_interface_port)
        self.external_routing_protocol = external_routing_protocol

    def print_routing_protocol(self):
        print(self.external_routing_protocol)


base_network_device = NetworkDevice(model="ISR/4331", manufacturer="Cisco")
print("Base network device")
print("print statement")
print(base_network_device)
print("Pretty print statement")
pprint(base_network_device)
print("hash")
print(hash(base_network_device))
base_network_device.boot_up()

router_network_device = NetworkRouter(
    model="ISR/4331", manufacturer="Cisco", routed_interface_port="Gi1/1"
)
print("router network device")
print("print statement")
print(router_network_device)
print("Pretty print statement")
pprint(router_network_device)
print("hash")
print(hash(router_network_device))
router_network_device.boot_up()

core_router_network_device = CoreRouter(
    model="ISR/4331",
    manufacturer="Cisco",
    routed_interface_port="Gi1/1",
    internal_routing_protocol="OSPF",
)
print("Core router network device")
print("print statement")
print(core_router_network_device)
print("Pretty print statement")
pprint(core_router_network_device)

core_router_network_device.boot_up()
core_router_network_device.print_routing_protocol()


boarder_router_network_device = BoarderRouter(
    model="ISR/4331",
    manufacturer="Cisco",
    routed_interface_port="Gi1/1",
    external_routing_protocol="bgp",
)
print("Core router network device")
print("print statement")
print(boarder_router_network_device)
print("Pretty print statement")
pprint(boarder_router_network_device)

boarder_router_network_device.boot_up()
boarder_router_network_device.print_routing_protocol()

print(isinstance(boarder_router_network_device, NetworkDevice))

# # print(f"Is base_network_device the same as router_network_device: {base_network_device == router_network_device}")
# # print(f"Is {cool_van} the same as {not_cool_van}: {cool_van == med_cool_van}")
