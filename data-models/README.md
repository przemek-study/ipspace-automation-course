# Deploy base config and VLAN service

Ansible playbooks generating base node config and VLAN service config. 

# Playbooks

These playbooks use JINJA2 templates to translate node and vlan service data models into an Arista compatible config.

*gen_conf_nodes.yml* - uses *build_nodes.j2* template to translate node model into the config. Resulting files are stored in the config/{{ hostname }} directory.

*gen_conf_vlan_service.yml* - uses *build_vlan_service.j2* template to translate node model into the config. Resulting files are stored in the config/{{ hostname }} directory.

# Data models

**Node data model** is stored per host in the *host_vars* directory. Each node model contains the following elements:

__site__ - Site (DC) this device is located at
__mgmt__ - IP/Prefix to be assigned to the management interface (Ma1)  
__loop__ - IP to be assigned to the loopback interface (Lo0)  
__mc__ - boolean value, enables/disables multicast routing on the node  
__ibgp__ - a list of the iBGP peers, each item holds *port* on which peer connects
__ospf__ - boolean value, enables/disables OSPF routing on the node  
__rp__ - boolean value, if present, makes this node a PIM RP  
__pim__ a list of interfaces on which to enable PIM-SM  
__ports__ a list of interfaces, each item holds interface _name_, _ip_, _speed_, _desc_, __peer__, and whether it's _ospf_ enabled  
__trunks__ if present, contains trunk interfaces, their native vlans and a list of allowed vlans  
__mlag__ if present, contains _ip_ and _port_, used to configure MLAG  

---

**VLAN service data model** is stored in the "vlan_service.yml" file.

Each VLAN service contains the following elements:

__client name__ - dictionary containing VLAN ids to be created for the client

__vlan id__ - dictionary describing particular VLAN. Each vlan has the following elements:
* __multicast__ - enables/disables vlan for the multicast
* __network__ - IP network assigned to this VLAN
* __nodes__ - nodes where this VLAN needs to be deployed
* __protocols__ - procotols that need to advertise this VLAN's IP space
* __mlag__ - specifies whether MLAGs will be configured in this VLAN