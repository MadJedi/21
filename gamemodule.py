#Игра модуль для игры ОЧКО

class Player(object):
    """Инициализакия игрока."""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ответ на вопрос."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Подсчёт количества игроков."""
    response = None
    while response not in range(low, high):
        response = int(input(question).lower())
    return response

if __name__ == "__main__":
    input("Нажмите ENTER чтобы выйти.")
