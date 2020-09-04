from random import random, Random
import random

from app.Controller.CardController import CardController
from app.Model.User import User
from app.Model.card import Card
from app.View.view import View

users = []
cards = []
final_choice_of_hokm = -1


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
                        if number_in_circle == 1:
                            break
                    else:
                        # TODO check raise number
                        score = int(score_temp)
                        hakem = i
        return score, hakem

    @staticmethod
    def add_cards_and_remove_cards(hakem):
        temp_cards = users[hakem].cards
        print('player number ', hakem)
        all_cards = CardController.get_instance().all_cards()
        for i in all_cards:
            if not i[2]:
                temp_cards.append(Card(i[1], i[0]))
        removes = []
        for card in temp_cards:
            print(card.number, card.type, end=' ')
        while True:
            View.remove_cards(removes)
            command = input()
            if command.split(" ").__len__() > 2:
                print("invalid command")
                continue
            if command == "submit" and len(removes) == 4:
                print("ok")
                break
            if command.split().__len__() == 1:
                unselected = int(command)
                removes.pop(unselected - 1)
                continue
            if command.split().__len__() == 2 and len(removes) < 4:
                str_number, str_type = command.split()
                number = int(str_number)
                type = -1
                if str_type == "gishniz":
                    type = 1
                if str_type == "pik":
                    type = 2
                if str_type == "del":
                    type = 3
                if str_type == "khesht":
                    type = 4
                for card in temp_cards:
                    if card.number == number and card.type == type:
                        removes.append(card)
                        break
                continue

    @staticmethod
    def put_card_in_game(current):
        cards_in_carpet = []
        max_number = 0;
        print("player number ", current, ": ", end='')
        current_number, current_type = map(int, input().split())
        max_number = current_number
        cards_in_carpet.append([current_number, current_type])

    def first_round(self):
        hakem = 1
        print("player number ", hakem, ": ")
        command = int(input())
        cards_in_carpet = []
        cards_in_carpet.append(users[hakem].cards[command - 1])

        pass

    def game_running(self):
        pass

    @staticmethod
    def check_winner_of_hand(cards):
        zamine = cards[0].type
        max_number = -1
        winner_of_the_hand = hakem
        current_player = hakem
        player_that_played = 0
        boresh = False
        for card in cards:
            if card.number > max_number and card.type == zamine and card.type != final_choice_of_hokm and not boresh:
                winner_of_the_hand = current_player
                max_number = card.number
            if card.type == final_choice_of_hokm and not boresh:
                boresh = True
                winner_of_the_hand = current_player
                max_number = card.number
            if card.type == final_choice_of_hokm and boresh and card.number > max_number:
                winner_of_the_hand = current_player
                max_number = card.number
            current_player = (current_player + 1) % 4
        return winner_of_the_hand

    @staticmethod
    def find_score_of_the_hand(cards):
        score = 5
        for card in cards:
            if card.number%5 == 5:
                score += card.number
            if card.number == 1:
                score += 10
        return score



PlayGame.start_game()
score, hakem = PlayGame.choose_hakem()
PlayGame.add_cards_and_remove_cards(hakem)
