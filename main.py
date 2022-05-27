from check_net_status import *

with openstack.connect(cloud='dev.veone.net', region_name='veone', project_name= 'karajan') as con:
    check = CheckProjectInstancesNetStatus(con)
    check.ping_instances(interface="admin-net")