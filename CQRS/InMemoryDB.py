
from typing import Dict
from UserModel import User

class InMemoryDB:
    def __init__(self):
        self.users: Dict[str, User] = {}
