from random import random, Random
import random

from app.Controller.CardController import CardController
from app.Model.User import User
from app.Model.card import Card
from app.View.view import View

users = []
cards = []


class PlayGame:

    @staticmethod
    def start_game():
        for i in range(4):
            counter = 0
            temp_cards = []
            while counter < 12:
                type = random.randint(1, 4)
                number = random.randint(1, 13)
                if CardController.get_instance().put_card_to_user(type, number) == 1:
                    temp_cards.append(Card(number, type))
                    counter += 1
            users.append(User(temp_cards))

    @staticmethod
    def choose_hakem():
        is_in_circle = [True, True, True, True]
        hakem = -1
        score = -1
        number_in_circle = 4;
        while number_in_circle != 1:
            for i in range(4):
                if is_in_circle[i]:
                    View.entekhab_view(i)
                    score_temp = input()
                    if score_temp == 'pass':
                        is_in_circle[i] = False
                        number_in_circle -= 1
                    else:
                        # TODO check raise number
                        score = int(score_temp)
                        hakem = i
        return score , hakem
PlayGame.choose_hakem()
