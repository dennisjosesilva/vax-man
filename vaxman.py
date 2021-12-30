from vaxman_game.Game import Game 
from vaxman_game.LevelSelector import LevelSelector
from vaxman_game.GameOverScreen import GameOverScreen

def main():
  level_selector = LevelSelector()
  level_filename = level_selector.get_selected_level()
  
  while level_filename:
    game = Game()
    has_won = game.start(level_filename)    
  
    game_over_screen = GameOverScreen(has_won)
    game_over_screen.start()

    level_selector = LevelSelector()
    level_filename = level_selector.get_selected_level()
    



if __name__ == "__main__":
  main()