from interface_game import IGame


class Leaderboard(IGame):
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
        return cls
    
    @classmethod
    def print(cls):
        "A class level method"
        print("-----------Leaderboard-----------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
        print()
    @classmethod
    def add_winner(cls, position: str, name: str):
        "A class level method"
        cls._table[position] = name