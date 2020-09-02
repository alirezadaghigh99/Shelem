from random import random, Random
import random

from app.Controller.CardController import CardController
from app.Model.User import User
from app.Model.card import Card

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
        for i in CardController.get_instance().all_cards():
            if i[2] == False:
                print(i)


