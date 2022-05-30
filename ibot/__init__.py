from typing import Any
from mattermostdriver import Driver

# ibot = Driver({
#     'url': '',
#     'login_id': '',
#     'password': '',
#     # 'scheme': 'https',
#     'port': 80,
#     # 'verify': False
# })

# ibot.ldap

# user=ibot.users.get_user_by_username("wkouassi")

class BotSession(object):
    
    __session = None
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def getBot(cls) -> Any :
        if cls.__session == None:
            cls.__session = cls()
        return cls.__session
    
