from check_net_status import *
import openstack

projects = []

for i in projects:
    print("=================== Project {} Check Up ======================\n".format(i))
    with openstack.connect  (cloud='', region_name='', project_name= i) as con:
        check = InstancesNetStatus(con)
        check.ping_instances(interface="") 