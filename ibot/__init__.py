from mattermostdriver import Driver

ibot = Driver({
    'url': '',
    'login_id': '',
    'password': '',
    # 'scheme': 'https',
    'port': 80,
    # 'verify': False
})

ibot.ldap

user=ibot.users.get_user_by_username("wkouassi")
