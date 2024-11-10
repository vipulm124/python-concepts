from InMemoryDB import InMemoryDB
from Commands.CreateUserCommand import  CreateUserCommand
from Commands.UpdateUserCommand import UpdateUserCommand
from uuid import uuid4
from UserModel import User

class UserCommandHandler:
    def __init__(self, db: InMemoryDB):
        self.db = db
    
    def handle_create_user(self, command: CreateUserCommand):
        user_id = str(uuid4())
        user = User(user_id=user_id, name=command.name, email=command.email)
        self.db.users[user_id] = user
        print(f"User Created: {user_id} | {command.name} | {command.email}")
        return user_id
    
    def handle_update_user(self, command: UpdateUserCommand):
        if command.user_id not in self.db.users:
            raise ValueError(f"UserId with ID {command.user_id} not found.")
        
        user = self.db.users[command.user_id]
        if command.name:
            user.name = command.name
        if command.email:
            user.email = command.email
        
        print(f"User updated: {command.user_id} | {command.name} | {command.email}")
