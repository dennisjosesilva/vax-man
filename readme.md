## Vax-Man Asigment

__developer__: Dênnis José da Silva

__email__: dennisjosesilva@gmail.com

Vax-Man is a game developed as an assignment (task) of the Forage Electronic Arts Software Engineering 
Virtual Experience Program. The assignment was to develop a game called Vax-man. This game is based 
on the game mechanics of Pacman. In this game, Pacman is replaced by Vax-man (a vaccine, in 
my implementation), the ghosts are replaced by viruses and the small energy balls are replaced by 
smiles (or people to be vaccinated). The roles are the following:

- Vax-Man kills the virus when Vax-Man comes to contact with it.
- Contact with a virus does not kill Vax-Man.
- Each Virus that was not killed by Vax-Man multiplies itself every 30 seconds.
- The game finishes with a win if Vax-Man vaccinates (collect) all people. It finishes 
  with a loss if the number of viruses grows to 32 times the initial number of viruses.

## Instructions

The game requires __Python 3.7__ and __pygame__ installed. To start, the player can just run 
the __vaxman.py__ file:

```shell
  foo@bar:~$ python vaxman.py
```

The first screen to appear is the Level Selector. The player can choose the level he/she wants to play
by pressing the Right or Left arrow of the keyboard. After being chosen, the player should press ENTER 
to play that level. The player can also quit the game by pressing ESC.

The first screen that appears is the Level Selector. The player can choose the level he/she wants to 
play by pressing the Right or Left arrow of the keyboard. After being chosen, the player should 
press ENTER to play that level. The player can also quit the game by pressing ESC.

## Inspirations

The implementations are inspired by 3 sources provided by Forage Electronic Arts Software Engineering Virtual Experience Program:

- pygame primer: https://realpython.com/pygame-a-primer/
- pacman example 1: https://github.com/hbokmann/Pacman
- pacman example 2: https://github.com/grantjenks/free-python-games/blob/master/freegames/pacman.py

The virus movements were implemented using the Dijkstra Algorithm to find the shortest path in graphs. The implementation randomly chooses a point in the level, and the shortest path from the virus to this point is computed. The implementation was based on the following link: 
https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra.

## Level Creation

The directory "levels" contains possible levels to be played. Custom levels can be created by adding a text 
file containing a text with the following characters:

- __p__: It must appear just one time, it indicates the initial position of the player.
- __v__: It must appear one or more times, they indicate the initial position of the virus.
- __0__: It must appear one or more times, they indicate the position of the people to be vaccinated.
- __1__: It can appear more than one time, they indicate the position of the walls.

To create a level, some rules must three rules be obeyed:

- Each row must have the same number of characters.
- The borders of a level that don't contain a wall, must also have a border at the oposite direction 
  with no walls (so the Vax-man that goes out of the screen appear at the other side of the screen).
- Each character must be separated by a space.

Some examples of level files are available at the __levels__ directory.

## Features To be Improved

Some improvements, I think I hope I can address in the future are:

- Make the game window at a fixed size. My initial implementation was considered a fixed level. 
  So, the game  window would have a fixed size. However, since I included the level editor the 
  level got a variable size. Consequently, the game window also got a variable size. 

  - To address it, I would like to choose a fixed window size. Then, positing the level 
    at the centre of the game window independently of the level size. Also, I would like to 
    fix the size of the game over screens.

- Improve the movement of the virus. At this point, the viruses do not consider the position 
  of the player, I think it would be the game a little more challenging with the virus trying 
  to avoid going close to the player (Vax-Man).

  - I think I can address it by including weight on the edges of the level graph.


- Include a timer, so the game could have a ranking to see who finishes the game first.
