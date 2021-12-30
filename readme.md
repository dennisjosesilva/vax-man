## Vax-Man Asigment

__developer__: Dênnis José da Silva

__email__: dennisjosesilva@gmail.com

Vax-Man is game developed as an assignment (task) of the Forage Eletronic Arts Software Engineering 
Virtual Experience Program. The assignment was to developed a game called Vaxman. This game is based 
on the game mechanism of Pacman. In this game, Pacman is replaced by the vaxman (a vaccine, in 
my implementation), the ghosts are replaced by viruses and the small energy balls are replaced by 
smiles (or people to be vaccined). The roles are the following:

- Vax-Man kills the virus when Vax-Man comes to contact with it.
- Contact with a virus does not kill Vax-Man.
- Each Virus that was not killed by Vax-Man multiplies itself every 30 seconds.
- The game finishes with a win, if Vax-Man vaccinates (collect) all people. It finishes 
  with a lose, if the number of viruses grows to 32 times the initial number of viruses.

## Instruction:

The game requires __Python 3.7__ and __pygame__ installed. To start one can just run the 
__vaxman.py__ file:

```shell
  foo@bar:~$ python vaxman.py
```

The first screen to appear is the Level Selector. The player can choose the level he/she wants to play
by pressing the Right or Left arrow of the keyboard. After chosen, the player should press ENTER to play that 
level. The player can also quit the game by pressing ESC.

During the game, the player moves the Vax-Man by using the arrow keys. When the game finishes, a game over 
screen appear and the player should press ENTER (Return) to go back to the Level Selector screen. This loop 
continues until the player press ESC at the Level Selector screen.

## Inspirations:

The implemtations are inspired by 3 sources provided by Forage Eletronic Arts Software Engineering 
Virtual Experience Program:

- pygame primer: https://realpython.com/pygame-a-primer/
- pacman example 1: https://github.com/hbokmann/Pacman
- pacman example 2: https://github.com/grantjenks/free-python-games/blob/master/freegames/pacman.py

The virus movements was implemented using the Dijkstra Algorithm to find the shortest path in 
graphs. The implementation randomly chooses a point in the level, and a path from the virus to 
this point is computed. The implementation was based on the following link: 
https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra.

## Level Creation:

The directory "levels" contains possible levels to be played. Custom levels can be create 
by adding a text file containing a text with the following characters:

- __p__: It must appear just one time, it indicates the initial position of the player.
- __v__: It must appear one or more time, they indicate the initial position of the virus.
- __0__: It must appear one or more time, they indicates the position of the people to be vaccinated.
- __1__: It can appear more than one time, it indicates the position of the walls.

To create a level, some rules must three rules be obeyed:

- Each row must have the same number of characters.
- The borders of a level that don't contain a wall, must also have a border at the oposite direction 
  with no walls (so the Vax-man that goes out of the screen appear at the other side of the screen).
- Each character must be separated by a space.

Some examples of level files are available at the __levels__ directory.

## Features To be Improved:

Some improvements, I think I hope I can address in the future are:

- Make the game window at a fix size. My initial implementation considered a fix level. So,
  the game window would have a fix size. However, since I included the level editor feature 
  the level got a variable size. Consiquently the game window also got a variable size. 

  - To address it, I would like to chose a fixed window size. Then, positing the level 
    at the center of the game window indepently of the level size. Also fix the size of
    the game over screens.

- Improve the movement of the virus. At this point, they do not consider the position of the player,
  I think it would be the game a little more challenge with the virus tries to avoid going close 
  to the player (Vax-Man).

  - I think I can address it by including weight to the edges of the level graph.



