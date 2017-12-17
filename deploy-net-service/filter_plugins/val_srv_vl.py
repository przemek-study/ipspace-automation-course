import json

# Validator for 'show vlan'
def vl_show_vlan(val_rules, cmd_out):
    result = {'txt': []}
    valid = True
    cmd = json.loads(cmd_out)
    for vid,v in val_rules['vlans'].iteritems():
        if str(vid) in cmd['vlans']:
            for st, stv in v.iteritems():
                if stv <> cmd['vlans'][str(vid)][st]:
                    valid = False
                    result['txt'].append(
                            "VLAN {} state is invalid, "
                            "value: {}, expected: {}"
                            .format(vid, st, stv))
    if valid:
        result['txt'].append(cmd)
    result['valid'] = valid
    return result


# Validator for 'sh interfaces trunk'
def vl_sh_int_trunk(val_rules, cmd_out):
    result = {'txt': []}
    non_compl_txt = []
    valid = True
    cmd = json.loads(cmd_out)
    for k,v in val_rules['trunks'].iteritems():
        if str(k) in cmd['trunks']:
            for vid in v['allowedVlans']['vlanIds']:
                if vid not in cmd['trunks'][k]['allowedVlans']['vlanIds']:
                     valid = False
                     result['txt'].append(
                             "Trunk {} state is invalid, "
                             "Vlan {} is not allowed"
                             .format(k, vid))
        else:
            valid = False
            result['txt'].append(
                    "Interface {} state is invalid, "
                    "it should be a trunk"
                    .format(k))
    if valid:
        result['txt'].append(cmd)
    result['valid'] = valid
    return result


# Dict mapping show_command to a validation function
val_func = {
    'show_vlan': vl_show_vlan,
    'show_interfaces_trunk': vl_sh_int_trunk,
}

# This function is called when filter in invoked
def val_srv_vlan(show_cmds, host, val_file):
    report = {'cmds': [], 'non_compl_txt': []}
    compliant = True
    for k,v in show_cmds.iteritems():
        # Only json commands are supported
        if not k.endswith("json"):
            continue
        # Get rid of ' | json' and replace spaces with '_'
        key = "_".join(k.split(" ")[:-2])
        if key not in val_file:
            print("{} not in the validation file, skipping".format(key))
        elif key in val_func:
            result = val_func[key](val_file[key], v)
            if not result['valid']:
                compliant = False
            report['cmds'].append(result)
        else:
            print("{} not supported".format(k))

    report['non_compl_txt'] += [i['txt'] for i in report['cmds'] if not i['valid']]
    report['compliant'] = compliant
    return report


class FilterModule(object):
    ''' URI filter '''

    def filters(self):
        return {
            'val_srv_vlan': val_srv_vlan
        }
