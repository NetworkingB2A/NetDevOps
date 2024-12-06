import sqlite3

connection = sqlite3.connect("device.db")

cursor = connection.cursor()




# # Creating table
sql_statements = ["""CREATE TABLE IF NOT EXISTS PRIMARYDEVICES (id INTEGER PRIMARY KEY, name TEXT, ip TEXT);""",
                  """CREATE TABLE IF NOT EXISTS DNACDEVICES (id INTEGER PRIMARY KEY, name TEXT, ip TEXT, device_type TEXT);""",]

for sql_statement in sql_statements:
    cursor.execute(sql_statement)

for id in range(1,10):
    cursor.execute(f"""INSERT INTO PRIMARYDEVICES (id, name, ip) VALUES ({id}, 'router{id}', '10.10.10.{id}/24') """) 
    cursor.execute(f"""INSERT INTO DNACDEVICES (id, name, ip, device_type) VALUES ({id}, 'router{id}', '10.10.10.{id}/24', 'router') """) 






connection.commit()
connection.close()


# connection = sqlite3.connect("device.db")
# cursor = connection.cursor()
# create_table = """CREATE TABLE IF NOT EXISTS PRIMARYDEVICES (pk INTEGER PRIMARY KEY, name TEXT, netbox_id INTEGER, ip TEXT, manufacture TEXT, platform TEXT);"""
# cursor.execute(create_table)

# # Add data to database

# devices = nb.dcim.devices.all()

# for device in devices:
#     insert_device = f"""INSERT INTO PRIMARYDEVICES (name, netbox_id, ip, manufacture, platform) VALUES ( '{device.name}', {device.id}, '{device.primary_ip4}', 'Cisco Systems, Inc', '{device.platform}' )"""
#     cursor.execute(insert_device)
#     # pprint(vars(device))

# connection.commit()
# connection.close()