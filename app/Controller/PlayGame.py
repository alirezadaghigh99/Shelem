from app.Model.User import User

users = []
cards = []

class PlayGame:

    @staticmethod
    def start_game():
        for i in range(4):
            users.append(User())


