# Deploy configs and validate them

A set of Ansible playbooks deploying and validating base, and vlan service, configs.

# Roles

*base* - Generates base config files using templates to translate node model.  
*vlan_service* - Generates vlan service files using templates to translate service model.  

# Playbooks

*deploy_configs.yml* - Uses roles *base* and *vlan_service* to generate config files and deploys them to the devices using Napalm. Stores diffs, if any.

*val_base* - Automatically validates base config using validation templates generated from the base model. Uses Napalm validation module.

*val_srvc_vlan* - Automatically validates vlan service config using custom Python filter "val_srv_vl.py". 

Config files are stored in the "configs" directory.
Validation rules are stored in the "validate" directory.

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
__ports__ a dictionary of interfaces, interface name is a key, values are its _ip_, _speed_, _desc_, __peer__, and whether it's _ospf_ enabled  
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