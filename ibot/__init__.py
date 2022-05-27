from mattermostdriver import Driver

ibot = Driver({
    'url': 'team.veone.net',
    'login_id': 'wkouassi',
    'password': 'AMD Quad-CoreA8',
    # 'scheme': 'https',
    'port': 80,
    # 'verify': False
})

ibot.ldap

user=ibot.users.get_user_by_username("wkouassi")
