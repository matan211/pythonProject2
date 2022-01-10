class Player:
    def __init__(self,id,num_of_cards,):
        self.id=id
        if num_of_cards>26 or num_of_cards <10:
            self.num_of_cards=26
        else:
            self.num_of_cards=num_of_cards
        self.player_package={}



    def set_hand(self,):

