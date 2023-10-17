from ExerciseRocket import RocketBoard
from ExerciseRocket import Rocket


board = RocketBoard(6)
board[0].x = 6
for rocket in board:
    print(rocket.id)
print(RocketBoard.get_distance(board[0], board[1]))
