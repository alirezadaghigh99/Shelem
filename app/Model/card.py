class Card:
    number = -1
    type = -1  # 1 for gishniz // 2 for pik // 3 for del // 4 for khesht
    is_used = False

    def __init__(self, number, type):
        self.type = type
        self.number = number
