from pprint import pprint
from jnpr.junos import Device
import getpass

import getpass
from jnpr.junos import Device
host = None
uname = None
pw = None
if host == None:
    host == input("Hostname or Ip: ")
if uname == None:
    uname == input("Username: ")
if pw == None:
    pw = getpass.getpass()
dev = Device(host=host,user=uname,password=pw)

dev.open()
pprint(dev.facts)
dev.close()