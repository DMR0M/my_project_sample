from dataclasses import dataclass, field


@dataclass()
class ListPrivileges:
    _privilege_1: str = 'can add post'
    _privilege_2: str = 'can delete post'
    _privilege_3: str = 'can ban user'


class Configurations:
    _configs: dict = {'connection': 'on', 'vpn': 'off', 'port': 1907}




