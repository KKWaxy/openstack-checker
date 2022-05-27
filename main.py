from check_net_status import *

with openstack.connect(cloud='', region_name='', project_name= '') as con:
    check = CheckProjectInstancesNetStatus(con)
    check.ping_instances(interface="admin-net")