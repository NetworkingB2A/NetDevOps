from scrapli.driver.core import IOSXEDriver
from scrapli import Scrapli

my_device = {
    "host": "192.168.1.241",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False
}

conn = IOSXEDriver(**my_device)
print("point 1")
conn.open()
print("point 2")
conn.send_command("terminal length 0")
print("point 3")
response = conn.send_command("show run")
print(response.result)