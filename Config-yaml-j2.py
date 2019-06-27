from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
from jinja2 import Template
import yaml
import sys

junos_hosts = ["vMX-1"]

for host in junos_hosts:
    with open(host + ".yml", "r") as yml_var:
        data = yaml.load(yml_var.read())
    with open("snmp.j2", "r") as j2_var:
        t_format = j2_var.read()
    template = Template(t_format)
    myConfig = template.render(data)
    print("\nResults for device " + host)
    print (myConfig)
    dev = Device(host=host, user="lab", password="lab123")
    dev.open()
    config = Config(dev)
    config.lock()
    config.load(myConfig, merge=True, format ="text")
    config.pdiff()
    config.commit()
    config.unlock()
    dev.close()
