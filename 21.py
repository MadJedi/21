#Игра 21 очко
import cardmodule,gamemodule 

class TO_Card(cardmodule.Card):
    """ Карты."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = TO_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class TO_Deck(cardmodule.Deck):
    """ Колода карт. """
    def populate(self):
        for suit in TO_Card.SUITS:
            for rank in TO_Card.RANKS:
                self.cards.append(TO_Card(rank, suit))

class TO_Hand(cardmodule.Hand):
    """ Набор карт одного игрока. """
    def __init__(self, name):
        super(TO_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(TO_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cardmodule:
            t += card.value

        contains_ace = False
        for card in self.cardmodule:
            if card.value == TO_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21

class TO_Player(TO_Hand):
    """ Игрок. """
    def is_hitting(self):
        response = gamemodule.ask_yes_no("\n" + self.name + ", хотите взять ещё? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "перебор.")
        self.lose()

    def lose(self):
        print(self.name, "проигрыш.")

    def win(self):
        print(self.name, "победа.")

    def push(self):
        print(self.name, "pushes.")

class TO_Dealer(TO_Hand):
    """ Раздающий """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебор.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class TO_Game(object):
    """ Игра. """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = TO_Player(name)
            self.players.append(player)

        self.dealer = TO_Dealer("Раздающий")

        self.deck = TO_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        #инициация двух карт
        self.Deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card() #скрыть первую карту раздающего
        for player in self.players:
            print(player)
        print(self.Dealer)
        #добавление карт
        for player in self.players:
            self.__additional_cards(player)
        self.Dealer.flip_first_card() 
        if not self.still_playing:
            #если все игроки перебрали карты показ руки дилера
            print(self.Dealer)
        else:
            print(self.Dealer)
            self.__additional_cardmodule(self.Dealer)
            if self.Dealer.is_busted():
                #для всех кто ещё не выбыл
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.Dealer.total:
                        player.win()
                    elif player.total < self.Dealer.total:
                        player.lose()
                    else:
                        player.push()                       
        for player in self.players:
            player.clear()
        self.Dealer.clear()

def main():
    print("\t\tДобро пожаловать в игру ОЧКО!\n")

    names = []
    number = gamemodule.ask_number("сколько будет игроков? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name)
    print()
    game = TO_Game(names)
    again = None
    while again != "n":
        game.play()
        again = gamemodule.ask_yes_no("\nСыграем ещё?: ")


main()
input("\n\nНажмите ENTER чтобы выйти.")
