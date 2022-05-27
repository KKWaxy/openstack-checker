import subprocess
import ipaddress
from time import sleep
import traceback

from typing import List, Union

from openstack.connection import Connection
from openstack.compute.v2.server import Server
import openstack

class CheckProjectInstancesNetStatus(object):
    
        def __init__(self, conn: Connection) -> None:
            
            self.conn = conn
            
        def list_servers(self) -> List[Server]:
            """_summary_

            Returns:
                List[Server]: _description_
            """
            return self.conn.compute.servers()
        
        def get_servers_ip4_by_interface(self, interface: str) -> List[str]:
            """_summary_

            Returns:
                List[str]: _description_
            """
            serv_ips = [] 
            for serv in self.list_servers():
                addresses = serv.addresses
                if not interface in addresses.keys():
                    msg = "Exception: {} does  not have {} interface".format(serv.name,interface)
                    print(msg)
                    continue
                else:
                    serv_ips.append(ipaddress.ip_address(addresses[interface][0]["addr"]))
            return serv_ips
        
        def ping_instances(self, instanceIP: Union[str,None] = None, interface: Union[str, None] = None) -> None:
            """_summary_

            Args:
                instanceIP (Union[str,None], optional): _description_. Defaults to None.
                interface (Union[str, None], optional): _description_. Defaults to None.

            Raises:
                Exception: _description_
            """
            global TEMP
            TEMP = 3
            
            def ping(ip: str) -> subprocess.CompletedProcess:
                """

                Args:
                    ip (str): _description_

                Returns:
                    subprocess.CompletedProcess: _description_
                """
                global TEMP 
                shell_str = "ping -c 4 {}".format(ip)
                process = subprocess.run(shell_str,shell=True,stdout=subprocess.PIPE, universal_newlines=True)
                if process.returncode != 0:
                    sleep(5)
                    TEMP -=1
                    if TEMP == 0:
                        return(process)
                    ping(ip)
                TEMP=3
                return(process)
                
            ips_to_ping = []
            EXCEPTION = [" ", None]
            
            if instanceIP != None:
                ips_to_ping.append(instanceIP)
            if interface != None:
                for serv_addr_v4 in self.get_servers_ip4_by_interface(interface):
                    ips_to_ping.append(serv_addr_v4)    
            if( instanceIP in EXCEPTION and interface in EXCEPTION):
                raise Exception("You must give an IP or Interface to ping.")
            for ip in ips_to_ping:    
                process = ping(ip)
                print(process.stdout)
                
        def netcat_ports(self, ports: Union[int, List[int]], instanceIp4: str) -> bool:
            
            def netcat(port: int):
                pass
            
            assert isinstance(ports,(int,list)),"Port mast be of type Int or a list of int "
            
            if isinstance(ports, int):
                pass
            else:
                pass
                
            return True