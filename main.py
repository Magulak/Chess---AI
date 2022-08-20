# Zamiast 5 zmiennych może klasa :)?
# zmiana w kodzie
#  Use numpy for loops on arrays (this should be wayyyyyyyy faster)
#  (type_of_piece)
class Chess:
    class Pawn:
        print("Class for pawns")

        def moveset(self, y, x, chess_board2):
           if chess_board2[y][x] == [2, 2]:
               print("czarny")
               chess_board2[y][x] = [7, 7]
               return chess_board2




    class Knight:
        print("Class for knights")

    class King:
        print("Class for kings")

    class Queen:
        print("Class for queens")

    class Bishop:
        print("Class for bishops")


    class Rook:
        print("Class for rooks")

    def move(self, board, x1, y1, x2, y2):
        """
        :param board: -  chess_board
        :param x1: - x coordinate of chess_piece that will be moved
        :param y1: - y coordinate of chess_piece that will be moved
        :param x2: - x coordinate of desired place
        :param y2: - y coordinate of desired place
        :return: return change chess_board to state after the move / deny if move is illegal
        """

        """  
        bishop movement is going to be represented by bishopmovement.png
        """

        def attack(self):
            print("attack")

        # If friendly piece encounters enemy piece on its move, the enemy piece gets destroyed

        print("if:"
              " \n - Desired spot is empty"
              " \n - Selected piece have move_set that allows him to move there"
              " \n - No checkmate")




    chess_board2 = [
        [[5, 2], [4, 2], [3, 2], [1, 2], [6, 2], [3, 2], [4, 2], [5, 2]],  # y0
        [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2]],  # y1
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y2
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y3
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y4
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y5
        [[2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1]],  # y6
        [[5, 1], [4, 1], [3, 1], [6, 1], [1, 1], [3, 1], [4, 1], [5, 1]]]  # y7
    #     x0       x1       x2     x3      x4       x5      x6      x7

    chess_board2 = Pawn.moveset(1, 1, 2, chess_board2)

    for x in range(len(chess_board2)):
         print(chess_board2[x])


    """
    chess_board[y] [x] [data]
    """

    """
    type_of_piece, Enemy/Ally)
    The King == 1
    The Pawn == 2
    The Bishop == 3
    The Knight == 4
    The Rook == 5
    The Queen == 6
    
    (0 , 0) == empty
    (x , 1) == white
    (x , 2) == black
    """
