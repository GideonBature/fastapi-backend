from app.exceptions.user import UserNotFoundError

class UserService:
    def get_user(self, user_id: int):
        if user_id < 1:
            raise UserNotFoundError("User not found")
        
        return {
            "id": user_id,
            "name": f"User {user_id}"
        }