class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return f"Player: {self.__name}" \
               f"\nSprint: {self.__sprint}" \
               f"\nDribble: {self.__dribble}" \
               f"\nPassing: {self.__passing}" \
               f"\nShooting: {self.__shooting}"

    @property
    def name(self):
        return self.__name
