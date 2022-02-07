from napalm import get_network_driver
from pprint import pprint


driver = get_network_driver('ios')
# Connect:
device = driver(
    hostname="192.168.1.241",
    username="cisco",
    password="cisco"
)
print("Opening ...")
device.open()

pprint(device.get_interfaces_ip())
#with driver('localhost', 'vagrant', 'vagrant', optional_args={'port': 12443}) as device:
#    print(device.get_facts())
#    print(device.get_interfaces_counters())