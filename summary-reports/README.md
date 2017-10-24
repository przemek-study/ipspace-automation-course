Solution to the "easy win: create summary reports" exercise.

# BGP peering report creator

*TODO* Make it Cisco compatible, currently only works with Arista devices.

This playbook, "create_bgp_report.yml" logs into devices and retrieves a list of BGP peers.

Once BGP peers are retrieved, the playbook will try, for each of the peers, to retrieve routes received, accepted, and advertised.

Once all of the data is collected a report will be created for each of the devices.

Reports are stored in the "reports" directory, in files with the name following the format "{hostname}_bgp_peers_report.txt".

Template used to generate the format is written in JINJA2, stored in "templates/bgp_peer_report.j2".

A few example reports can be found in "reports".

Also, one full example report is included below:


'''
===========================================================================
========== BGP peerings report for: vEOS-02 ============
===========================================================================

=======================================================
============= Peer: 10.0.12.1 ==============
=======================================================

Peer AS: 65001
Status: Established
Number of routes received from the peer: 4
Number or routes accepted from the peer: 4



=========== Prefixes received =================
  - Prefix: 192.168.7.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1
  - Prefix: 192.168.4.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1
  - Prefix: 192.168.6.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1
  - Prefix: 192.168.5.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1



=========== Prefixes accepted =================
  - Prefix: 192.168.7.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1
  - Prefix: 192.168.4.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1
  - Prefix: 192.168.6.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1
  - Prefix: 192.168.5.0/24, Next Hop: 10.0.12.1 , AS Path: i Or-ID: 192.168.4.1 C-LST: 10.0.13.1



=========== Prefixes advertised =================
  - Prefix: 192.168.0.0/24, Next Hop: 10.0.12.2 , AS Path: i
  - Prefix: 192.168.2.0/24, Next Hop: 10.0.12.2 , AS Path: i
  - Prefix: 192.168.1.0/24, Next Hop: 10.0.12.2 , AS Path: i
  - Prefix: 192.168.3.0/24, Next Hop: 10.0.12.2 , AS Path: i
'''

# ipspace-automation-course