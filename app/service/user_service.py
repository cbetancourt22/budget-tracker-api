from app.repository.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def get_all_users(self):
        # Example business logic
        return self.repo.get_all()
