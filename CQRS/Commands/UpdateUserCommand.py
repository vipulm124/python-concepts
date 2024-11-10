from typing import Optional


class UpdateUserCommand:
    def __init__(self, user_id: str, name: Optional[str] = None, email: Optional[str] = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        

