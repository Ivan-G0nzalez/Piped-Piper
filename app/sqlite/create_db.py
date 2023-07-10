import sqlite3

conn = sqlite3.connect('app/db/data.db')

c = conn.cursor()

# c.execute("""CREATE TABLE components (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(25) NOT NULL,
# status INTEGER DEFAULT 1
# ) """)

c.execute("""
    CREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_count INTEGER,
    cpu_utilization INTEGER,
    firmaware_version VARCHAR(15),
    labels TEXT,
    macaddr TEXT,
    mem_free INTEGER,
    mem_total INTEGER,
    model TEXT,
    name VARCHAR(25) NOT NULL,
    serial TEXT,
    stack_id INTEGER,
    status TEXT DEFAULT Up,
    temperature TEXT,
    uptime INTEGER,
    uplink_ports TEXT,
    components_id INTEGER,
    FOREIGN KEY (components_id) REFERENCES components(id)
    )
""")

# c.execute("""
#     INSERT INTO devices (
#     client_count,
#     cpu_utilization,
#     firmaware_version,
#     labels,
#     macaddr,
#     mem_free,
#     mem_total,
#     model,
#     name,
#     serial,
#     stack_id,
#     status,
#     temperature,
#     uptime,
#     uplink_ports
#     ) VALUES (
#     0,
#     0,
#     "",
#     "",
#     "",
#     0,
#     0,
#     "",
#     'switch123',
#     123456,
#     0,
#     'up',
#     40,
#     10,
#     'prueba'
#     )
# """)

# c.execute("""
#     INSERT INTO devices (
#     name,
#     serial,
#     status,
#     temperature,
#     uptime,
#     uplink_ports
#     ) VALUES (
#     device123,
#     123456,
#     status,
#     up,
#     47,
#     prueba
#     )
# """)


conn.commit()

conn.close()
