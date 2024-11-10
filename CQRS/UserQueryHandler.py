from InMemoryDB import InMemoryDB

class UserQueryHandler:
    def __init__(self, db: InMemoryDB):
        self.db = db
    
    def get_user_by_id(self, user_id: str):
        return self.db.users.get(user_id)
    

    def list_users(self):
        return list(self.db.users.values())