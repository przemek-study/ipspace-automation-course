import ipaddress as ip

def get_peer_info(pd, hostvars):
    peer = { 'name': pd['peer'] }
    our_net = ip.IPv4Interface(pd['ip']).network
    pvars = hostvars[peer['name']]

    for k,v in pvars['ports'].iteritems():
        if not v['ip']:
            continue
        peer_nobj = ip.IPv4Interface(v['ip'])
        if our_net == peer_nobj.network:
            peer['ip'] = peer_nobj.ip
            break
    return peer
  
class FilterModule(object):
    ''' URI filter '''

    def filters(self):
        return {
            'get_peer_info': get_peer_info
        }
