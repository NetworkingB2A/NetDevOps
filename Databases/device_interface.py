import sqlite3
import pynetbox
import pathlib
from pprint import pprint
from sqlalchemy import text
import sqlalchemy



pathlib.Path.unlink("device.db", missing_ok=True)


engine = sqlalchemy.create_engine("sqlite+pysqlite:///:memory:", echo=True)

# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())


with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()


with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )

# use Nornir for speed
# nornir_netbox for inventory
# Log into device
# grab LLDP Neighbor, CDP neighbor throw into database

# https://github.com/twin-bridges/nornir_course/tree/master

# https://pynet.twb-tech.com/class-nornir.html