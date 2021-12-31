import random
class dicerollsim:
    """Dice Rolling Simulator"""

    def __init__(self):
        self._score = 0
        self._diceFaces = [1,2,3,4,5,6]
    
    def start_game(self,**cheats):
        print(">> \a\a DICE \a\a ROLL \a\a SIMULATOR \a\a <<")
        print(">>> Press Enter To Roll")
        
        while True:
            for k,v in cheats.items():
                if k == "cheats" and v == True:
                    self.rolled = random.randint(10000,100000)
                else:
                    self.rolled = random.choice(self._diceFaces)
            roll = input("|| ")
            self._score += self.rolled
            if roll == "":
                print(f'rolled {self.rolled} \nscore {self._score}')


if __name__ == '__main__':
    drs = dicerollsim()
    drs.start_game(cheats=True)