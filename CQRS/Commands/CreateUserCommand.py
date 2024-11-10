from typing import Optional


class CreateUserCommand:
    def __init__(self, name: Optional[str], email: Optional[str]):
        self.name = name
        self.email = email
        

