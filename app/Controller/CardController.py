all_cards = []


class CardController:
    instance = None

    @staticmethod
    def get_instance():
        if CardController.instance is None:
            CardController()
        return CardController.instance

    def __init__(self):
        if CardController.instance is not None:
            raise Exception('this is a singleton!')
        else:
            CardController.instance = self
        for i in range(1, 5):
            for j in range(1, 14):
                all_cards.append([i, j, False])
        print(all_cards)

    @staticmethod
    def put_card_to_user(i, j):
        if not all_cards[(i - 1) * 13 + j-1][2]:
            all_cards[(i - 1) * 13 + j-1][2] = True
            return 1
        else:
            return -1
    def all_cards(self):
        return all_cards

