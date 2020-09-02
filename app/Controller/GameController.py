from app.View.view import View


class GameController:
    instance = None

    @staticmethod
    def get_instance():
        if GameController.instance is None:
            GameController()
        return GameController.instance

    def __init__(self):
        if GameController.instance is not None:
            raise Exception('this is a singleton!')
        else:
            GameController.instance = self

    def start_game(self):
        View.start_game_view()


