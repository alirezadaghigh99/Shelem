class View:
    @staticmethod
    def start_game_view():
        print("Game has started")
    @staticmethod
    def entekhab_view(i):
        print('player number ', i, 'read: ',end='')

    @staticmethod
    def remove_cards(list):
        l = len(list)
        if l == 0:
            print("you selected nothing yet please enter first card you wand to remove: ", end='')
        else:
            print("you already selected : ", end='')
            for i in range(l):
                print(list[i].number,end='')
                if list[i].type == 1:
                    print("gishniz, ",end='')
                if list[i].type == 2:
                    print("pik, ",end='')
                if list[i].type == 3:
                    print("del, ",end='')
                if list[i].type == 4:
                    print("khesht, ",end='')
            print("if you want to unselect one of them, type index of card in this list ",end='')
            if (l<4):
                print("or type the card that you want to select: ",end='')






