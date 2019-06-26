from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import getpass

host = None
uname = None
pw = None
if host == None:
    host = input("Hostname or IP: ")
if uname == None:
    uname = input("Username: ")
if pw == None:
    pw == getpass.getpass()

dev = Device(host=host, user=uname, password=pw, gather_facts=False)
dev.open()
cu = Config(dev)
diff = cu.diff()
if diff:
    cu.rollback()
dev.close()
