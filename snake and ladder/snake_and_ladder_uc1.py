import random 


class Player:

    def _init_ (self, name):
        self.name = name
        self.position = 0
        self.roll = 0

class GamePlay:

    def _init_ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.dice = 0
        self.turn = 0
        self.winner = ""

    def change_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def get_turn(self,option,player_position):
        if option == "snake":
            player_position -= self.dice
            if player_position < 0:
                player_position = 0
            self.change_turn()
        elif option == "ladder":
            player_position += self.dice
            if player_position > 100:
                player_position -= self.dice
            self.roll_dice()
        else :
            self.change_turn()
        return player_position
    
    def roll_dice(self):
        self.dice = random.randint(1,6)
        option = random.choice(["snake", "ladder", "no play"])
        if self.turn == 0:
            # self.get_turn(option, self.player1.position)
            self.player1.position = self.get_turn(option, self.player1.position)
            self.player1.roll += 1
        else:
            self.player2.position = self.get_turn(option, self.player2.position)
            self.player2.roll += 1
        
    
    def play(self):
        while (self.player1.position!= 100 and self.player2.position != 100):
            self.roll_dice()

        if self.player1.position == 100:
            self.winner = self.player1.name
            print("Position is ", self.player1.position)
            print("Rolls is ", self.player1.roll)
            print("winner is ", self.winner)
        else:  
            self.winner = self.player2.name
            print("Position is ", self.player2.position )
            print("Rolls is ", self.player2.roll)
            print("winner is ", self.winner)
        
player1 = Player("player1")
player2 = Player("player2")

game = GamePlay(player1, player2)
game.play()