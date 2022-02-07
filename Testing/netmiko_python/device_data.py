from netmiko import ConnectHandler

my_device = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.241',
    'username': 'cisco',
    'password': 'cisco'
}

net_connect = ConnectHandler(**my_device)
output = net_connect.send_command('show ip int brief')
print(output)