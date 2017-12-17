import ipaddress as ip
import json

def val_vlan(cmd_out, services):
    pass


def val_serv_vlan(show_cmds, services, host):
    compliant = True
    for cl, vlans in services.iteritems():
        for vid, vdata in vlans.iteritems():
             if host in vdata['nodes']:
                 val_vlan(show_cmds['show vlan | json'], services)
                 print("{} host is here".format(host))
    for k, v in show_cmds.iteritems():
        print k, v
    print(show_cmds.keys())
    print(type(show_cmds))
    print(services)
    print(host)

    return compliant

class FilterModule(object):
    ''' URI filter '''

    def filters(self):
        return {
            'val_serv_vlan': val_serv_vlan
        }
