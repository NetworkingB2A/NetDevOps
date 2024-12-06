from pprint import pprint


class RoutingProtocol:
    def __init__(self, routing_protocol, administrator_distance, metric):
        self.routing_protocol = routing_protocol
        self.administrator_distance = administrator_distance
        self.metric = metric

    def print_routing_protocol(self):
        print(self.routing_protocol)


class InternalRoutingProtocol(RoutingProtocol):
    def __init__(
        self, routing_protocol, administrator_distance, metric, bandwidth_cost
    ):
        super().__init__(routing_protocol, administrator_distance, metric)
        self.bandwidth_cost = bandwidth_cost


class ExternalRoutingProtocol(RoutingProtocol):
    def __init__(self, routing_protocol, administrator_distance, metric, asn):
        super().__init__(routing_protocol, administrator_distance, metric)
        self.asn = asn


class NetworkDevice:
    def __init__(self, hostname, model, manufacturer, **kwargs):
        self.hostname = hostname
        self.model = model
        self.manufacturer = manufacturer
        self.kwargs = kwargs

    def __str__(self):
        """Represents this object as a string for pretty-printing"""
        return f"""
Object name: {self.__class__.__name__} 
  hostname: {self.hostname}
  model: {self.model}
  manufacturer: {self.manufacturer}
    """

    def boot_up(self):
        print("Network Device is now booting up")


class NetworkRouter(NetworkDevice):
    def __init__(
        self, hostname, model, manufacturer, routed_interface_port, routing_protocol
    ):
        super().__init__(hostname, model, manufacturer)
        self.routed_interface_port = routed_interface_port
        self.routing_protocol = routing_protocol

    def __str__(self):
        """Represents this object as a string for printing"""
        return f"""
Object name: {self.__class__.__name__} 
  model: {self.model}
  manufacturer: {self.manufacturer}
  routing_protocol: {self.routing_protocol.routing_protocol}
    """

    def boot_up(self):
        print("Network Router is now booting up")


external_pr = ExternalRoutingProtocol(
    routing_protocol="bgp", administrator_distance="20", metric="5", asn="64555"
)
external_router = NetworkRouter(
    hostname="boarder_router",
    model="ISR/4331",
    manufacturer="Cisco",
    routed_interface_port="gi0/0/1",
    routing_protocol=external_pr,
)
internal_pr = InternalRoutingProtocol(
    routing_protocol="ospf",
    administrator_distance="110",
    metric="10",
    bandwidth_cost="100",
)
internal_router = NetworkRouter(
    hostname="core_router",
    model="ISR/9500",
    manufacturer="Cisco",
    routed_interface_port="gi1/0/1",
    routing_protocol=internal_pr,
)
sd_wan_external_router = NetworkRouter(
    hostname="sd_wan_router",
    model="850",
    manufacturer="Cisco-Meraki",
    routed_interface_port="gi0/0/1",
    routing_protocol=ExternalRoutingProtocol(
        routing_protocol="RIP", administrator_distance="100", metric="100", asn="11111"
    ),
)

pprint(external_pr)
external_pr.print_routing_protocol()
pprint(internal_pr)
internal_pr.print_routing_protocol()
print(external_router)
external_router.routing_protocol.print_routing_protocol()
print(internal_router)
internal_router.routing_protocol.print_routing_protocol()
print(sd_wan_external_router)
sd_wan_external_router.routing_protocol.print_routing_protocol()
