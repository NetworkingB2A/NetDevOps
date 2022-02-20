from scrapli import Driver

MY_DEVICE = {
    "host": "192.168.1.241",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "ssh_config_file": "/etc/ssh/ssh_config"
}
conn = Driver(**MY_DEVICE)
conn.open()

print(conn.channel.get_prompt())
print(conn.channel.send_input("show run | i hostname")[1])

    # paging is NOT disabled w/ Scrape driver!
conn.channel.send_input("terminal length 0")
print(conn.channel.send_input("show run")[1])
conn.close()