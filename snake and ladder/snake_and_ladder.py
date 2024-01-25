import random

class Player:
    def __init__(self , name):
        self.name = name
        self.position = 0
       
    def move_forward(self , move_by):
        if not self.position + move_by >100 :
            self.position += move_by
       
    def move_backward(self , move_by):
        self.position -= move_by        
        if self.position < 0:
            self.position = 0

class Game:
    def __init__(self, players: list):
        self.player1, self.player2 = players
        self.player_turn = 1
   
    @staticmethod  
    def roll_dice():
        return random.randint(1,6)
   
    def move_player_position(self, player):
        player: Player
        tile_play = random.choice(['snake' , 'ladder' , 'no_play'])
        dice_value = self.roll_dice()
       
        if tile_play == 'snake':
            player.move_backward(dice_value)
            self.player_turn = 2 if self.player_turn == 1 else 1                  
           
        elif tile_play == 'ladder':  
            player.move_forward(dice_value)
        else:
            self.player_turn = 2 if self.player_turn == 1 else 1                  

       
    def play(self):
        while self.player1.position < 100 and self.player2.position < 100 :
            if self.player_turn == 1 :
                self.move_player_position(self.player1)
            else:
                self.move_player_position(self.player2)


if __name__ == "__main__":
    player1 = Player('1')
    player2 = Player('2')
   
    game = Game([player1, player2])
    game.play()
    print(player1.position, player2.position)