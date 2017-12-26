def get_vlans(services, host):
    vlans = {}
    for cl, cldata in services.iteritems():
        for vid, vdata in cldata.iteritems():
            if host in vdata['nodes']:
                vlans[vid] = cl
    return vlans


helpers = {
    'get_vlans': get_vlans,
}


def vl_srv_helper(services, get_help, host):
    if get_help in helpers:
        result = helpers[get_help](services, host)
    else:
        result = "Helper {} not found".format(get_help)
    return result

class FilterModule(object):
    ''' URI filter '''

    def filters(self):
        return {
            'vl_srv_helper': vl_srv_helper
        }
