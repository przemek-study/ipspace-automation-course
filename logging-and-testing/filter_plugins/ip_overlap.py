from ipaddress import IPv4Network as ipv4

def ip_overlap(networks, ip_to_check):
    ipv4_tc = ipv4(ip_to_check)
    ipv4_nets = [ipv4(i) for i in networks if i != ip_to_check]
    overlap = sum([ipv4_tc.overlaps(i) for i in ipv4_nets])

    if overlap > 0:
        return True
    return False

class FilterModule(object):
    ''' URI filter '''

    def filters(self):
        return {
            'ip_overlap': ip_overlap
        }
